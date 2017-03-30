# - *-  coding: utf- 8 - *-
"""
    Siemens S7-400 data acquisition server
    
    This program was written using the python-snap7 module and the snap7 library.
    A configfile must exist (default file is aqserver.cfg) that defines
    communication and other parameters and of course the S7 variables to scan.
    Open this file in your preferred editor and read the comments on how to
    configure.
    Values will be stored to a csv-file, name can be configured, in subdirectory data.
    When program is stopped, this file will be compressed and stored to a path, 
    that can also be specified in the config file.
    
    Reading data from S7-400 using multireadvar
    - reading settings for 
        communication: IP, rack and slot
        miscellaneous settings: delimiter for datafile, file-name prefix
        trigger settings
        debug settings
        value settings: name, address, type  (reading from data blocks only!!)
    from config file
    
    - write data samples to csv file 
    - this file is gzipped when program is stopped by user or trigger occurs
    - close connection
    - close file

"""
#import main libs
from time import sleep
import sys
import os
import shutil
import ctypes
import struct
import logging
import collections
import random
import datetime

# Windows
if os.name == 'nt':
    from win32com.shell import shell, shellcon

# Posix (Linux, OS X)
else:
    pass


# import snap7 functions - S7 communication library
import snap7
from snap7.common import check_error
from snap7.snap7types import S7DataItem, S7AreaDB, S7WLByte
from snap7.util import *

# import my modules
import FileUtils
import TimeUtils
from S7Utils import get_S7_area, get_data_item
import CommUtils
import PrgUtils

# from KbdUtils import *
from kbhit import *

# get system arguments
###############################################################################
# define the config file
###############################################################################

if type(PrgUtils.parse_sys_args()) is list or type(PrgUtils.parse_sys_args()) is tuple:
    configfile = PrgUtils.parse_sys_args()[0]
else:
    configfile = PrgUtils.parse_sys_args()

# in Windows use My Documents directory    
if os.name == 'nt':
    # check for Aqserver in "My Documents" directory
    userdir = str(shell.SHGetFolderPath(0, shellcon.CSIDL_PERSONAL, None, 0))
    userdir = userdir.replace("\\","\/")    + "\/Aqserver\/"
# in Posix use home directory
else:
    username = PrgUtils.get_username()
    userdir = "\/home\/" + username + "\/Aqserver\/" 

# make data directory path
MyDataDir = userdir + "data\/" 

# make log directory path
MyLogDir = userdir + "log\/" 

# make directories if not existing
if not os.path.exists(userdir):
    os.mkdir(userdir)

if not os.path.exists(MyDataDir):
    os.mkdir(MyDataDir)

if not os.path.exists(MyLogDir):
    os.mkdir(MyLogDir)


# check configfile
if not os.path.isfile(configfile):
    print "config file %s does not exist, or no config filename given.\nUse aqserver --help!\n" %configfile
    sys.exit(0)

###############################################################################
# get all settings from configfile
###############################################################################
try:
    aqdata, com,  misc, value, trigger, dbg = PrgUtils.get_config(configfile)
except:
# sorry, no log because logfile not defined yet
#    logentry = "error in configfile!\nProgram will exit.\n"
#    logger.debug(" %s: %s" %(TimeUtils.getTS(), logentry))
    print "error in configfile!\nProgram will exit.\n"
    sys.exit(0)
    
###############################################################################
# debug settings
###############################################################################

# debug level
dbglevel = int(dbg["dbglevel"])
if dbglevel > 0  and dbglevel < 2:
    doInfo = True
else:
    doInfo = False
if dbglevel > 0  and dbglevel < 3:
    doWarning = True
else:
    doWarning = False
if dbglevel > 0  and dbglevel < 4:
    doDebug = True
else:
    doDebug = False
if dbglevel > 0  and dbglevel < 5:
    doError = True
else:
    doError = False
if dbglevel > 0  and dbglevel < 6:
    doCritical = True
else:
    doCritical = False

# remove the old log files
# call function to empty the folder
FileUtils.purgeDir(MyLogDir,1)

# logfile name
if bool(dbg["logts"]):
# can't use filename from config, because name has to be unique
#    logfile = MyLogDir + "\/" + dbg["logfile"] + str(TimeUtils.getTSfName()) +".log"
    logfile = MyLogDir + "\/" + misc["datafileprefix"] + str(TimeUtils.getTSfName()) +".log" 
else:
# can't use filename from config, because name has to be unique
#    logfile = MyLogDir +"\/" + dbg["logfile"] +  + ".log"
    logfile = MyLogDir +"\/" + misc["datafileprefix"] +  + ".log"

###############################################################################
# prepare logging
###############################################################################
# Numeric logging level for the message (DEBUG, INFO, WARNING, ERROR, CRITICAL)
logging.basicConfig(filename=logfile)
logger = logging.getLogger(__name__)
# logger.setLevel(logging.DEBUG)
logger.setLevel(logging.INFO)

#always log program start
logentry = "################## program started ###########################"
logger.info(" %s: %s" %(TimeUtils.getTS(), logentry))
logger.setLevel(dbglevel)


# write settings also to logfile, if debug is set
if doDebug:
    # communication settings
    logentry = str(com)
    logger.debug(" %s: %s" %(TimeUtils.getTS(), logentry))
    #miscellaneous settings
    logentry = str(misc)
    logger.debug(" %s: %s" %(TimeUtils.getTS(), logentry))
    # trigger
    logentry = str(trigger)
    logger.debug(" %s: %s" %(TimeUtils.getTS(), logentry))
    # debug
    logentry = str(dbg)
    logger.debug(" %s: %s" %(TimeUtils.getTS(), logentry))
    # values
    logentry = str(value)
    logger.debug(" %s: %s" %(TimeUtils.getTS(), logentry))

###############################################################################
# define communication
###############################################################################

# demo flag
if int(str(com["demo"])) == 1:
    demo = True
else:
    demo = False


# IP-address
IP = str(com["ip"])

# Validate IP address
if CommUtils.is_valid_ipv4_address(IP):
    if doDebug:
        logentry = "successfully checked IP address: " + str(IP)
        logger.debug(" %s: %s" %(TimeUtils.getTS(), logentry))
else:
    print "IP address not valid: %s, program exits!" %IP
    if doError:
        logentry = "wrong IP address: " + str(IP) + ", program stopped"
        logger.error(" %s: %s" %(TimeUtils.getTS(), logentry))
    sys.exit(0)
    
# rack number
RACK = int(com["rack"])
# slot number
SLOT = int(com["slot"])
# max. number of connect attempts
maxattempts = int(com["maxattempts"])

###############################################################################
# define miscellaneous settings
###############################################################################

if int(str(misc["usedir"])) == 1:
    usedir = True
else:
    usedir = False

fName = str(MyDataDir + "\/" + misc["datafile"] + ".csv")

# set the sleep time for every loop
scantime = float(misc["scantime"]) / 1000
# minimum scantime is 20 ms
# scantime is dependant on number of variables to scan !!!!
if scantime < 0.02 or demo:
    scantime = 0.02

if doDebug:
    logentry = "scantime in [s]: %f" % scantime
    logger.debug(" %s: %s" %(TimeUtils.getTS(), logentry))

maxrecords = int(misc["maxrecords"])

if doDebug:
    logentry = "maximum number of records: %d" % maxrecords
    logger.debug(" %s: %s" %(TimeUtils.getTS(), logentry))

if int(str(misc["booloffset"])) == 1:
    booloff = True
else:
    booloff = False
    
###############################################################################
# define trigger settings
###############################################################################

# check if trigger defined
if str(trigger["trgsignal"]) != "0":
    # set the do_trigger flag
    do_trigger = True
    # create the trigger expression
    trgexpression = str("trgsignal" + str(trigger["trgcondition"]) + str(trigger["trgvalue"]) )
    if doDebug:
        logentry = str(trgexpression)
        logger.debug(" %s: %s" %(TimeUtils.getTS(), logentry))

    # calculate number of pre- and post-trigger records
    prerec = int(int(float(trigger["pretrg"])/scantime))
    if doDebug:
        logentry = "pre-trigger records: %d" % prerec
        logger.debug(" %s: %s" %(TimeUtils.getTS(), logentry))
        
    postrec = int(int(float(trigger["posttrg"])/scantime))
    if doDebug:
        logentry = "post-trigger records: %d" % postrec
        logger.debug(" %s: %s" %(TimeUtils.getTS(), logentry))

    # add pre- and post-records. These will be copied from old to new record file
    # when a trigger occurs
    copyrec = prerec + postrec
    
else:
    # reset the no_trigger flag
    do_trigger = False
    trgexpression = str("False")
    copyrec = 0
# reset the trigger event flag
triggered = False
    
    
###############################################################################
# connect to PLC
###############################################################################

attempts = 0
# check if running in demo
if not demo:
    client = snap7.client.Client()
    clientConnected = False
    # try to connect
    while not clientConnected:
        attempts += 1
        try:
            client.connect(IP,RACK,SLOT)
        except:
            print "not connected, %d attempts" %attempts
            pass
        else:
            clientConnected = True
            if doDebug:
                logentry = "client connected"
                logger.debug(" %s: %s" %(TimeUtils.getTS(), logentry))
        if attempts >= maxattempts and maxattempts!= 0:
            if doError:
                logentry = "error when trying to connect, program will end!"
                logger.error(" %s: %s" %(TimeUtils.getTS(), logentry))
            print "error when trying to connect, program will end!"
            sys.exit(0)

###############################################################################
# define value settings
###############################################################################

# only 20 values per multiread
calls = (len(value) // 20) + 1

# remainder 
remain = len(value) % 20

if doDebug:
    logentry = "Calls: %d, Remainder: %d Gesamt : %d" % (calls,remain, len(value))
    logger.debug(" %s: %s" %(TimeUtils.getTS(), logentry))

# define our items
lvariables = []
lformats = []
lnames = []

for x in range(calls):
    if x < calls -1:
        lvariables.append((S7DataItem * 20)())
    else:
        lvariables.append((S7DataItem * remain)())
if doDebug:
    logentry = str(lvariables)
    logger.debug(" %s: %s" %(TimeUtils.getTS(), logentry))

# preset S7 area
area=0x84

# reset loop counters
cntcalls = 0
cntitems = 0
formats =[]
names = []
data_items = lvariables[0]

    
# add number and timestamp to file header
header = "number" + misc["delimiter"] + "timestamp" +  misc["delimiter"]


# loop through values and define the items
for val in value:
    
    mem = str(value[val])
    #######################################
    # get area
    #######################################
    name = str(val)
    names.append(name)
    area = get_S7_area(mem)
    dbnum,length, start, format, hdr = get_data_item(area, mem, name, misc["delimiter"])
    formats.append(format)
    header = header + hdr
    
    
    #######################################################################
    # now we check every single item by reading it once from PLC
    # if we have a problem we exit because of wrong congiguration
    #######################################################################

    configok = True 
    
    # check only when not in demo
    if not demo:
        try:
            result = client.read_area(area, dbnum, start, length)
        except:
            if doError:
                logentry = "Item %s does NOT exist in PLC. area: %d, dbnum: %d, start: %d. length: %d\n" %(mem, area,dbnum,start, length)
                logger.error(" %s: %s" %(TimeUtils.getTS(), logentry))
            configok = False
            pass
        else:
            if doDebug:
                logentry = "Item %s does exist in PLC\n" %mem
                logger.debug(" %s: %s" %(TimeUtils.getTS(), logentry))

    # finally write results in our items as C-type variables for snap7.DLL
    data_items[cntitems].Area = ctypes.c_int32(area)
    data_items[cntitems].WordLen = ctypes.c_int32(S7WLByte)
    data_items[cntitems].Result = ctypes.c_int32(0)
    data_items[cntitems].DBNumber = ctypes.c_int32(dbnum)
    data_items[cntitems].Start = ctypes.c_int32(start)
    data_items[cntitems].Amount = ctypes.c_int32(length)

    # increase the item counter
    cntitems += 1

    if doDebug:
        logentry = "area: %r" % area
        logger.debug(" %s: %s" %(TimeUtils.getTS(), logentry))
        logentry = "dbnum: %r" % dbnum
        logger.debug(" %s: %s" %(TimeUtils.getTS(), logentry))
        logentry = "start: %r" % start
        logger.debug(" %s: %s" %(TimeUtils.getTS(), logentry))
        logentry = "length: %r" % length
        logger.debug(" %s: %s" %(TimeUtils.getTS(), logentry))
    
    if cntitems >= 20 :
        cntitems = 0
        cntcalls +=1
        lvariables.append(data_items)
        lformats.append(formats)
        lnames.append(names)
        data_items = lvariables[cntcalls]
        if doDebug:
            logentry = "formats: %r" % formats
            logger.debug(" %s: %s" %(TimeUtils.getTS(), logentry))
        formats = []
        names = []
    
if cntitems < 20 :
    lvariables.append(data_items)
    lformats.append(formats)
    lnames.append(names)
    if doDebug:
        logentry = "formats: %r" % formats
        logger.debug(" %s: %s" %(TimeUtils.getTS(), logentry))
    formats = []
    names = []
    
if not configok:
    print "configuration fault, check most recent logfile %s!\n" %logfile
    sys.exit(0)
###############################################################################
# open record.csv for data recording (writing)
###############################################################################
# open file for data output
myOutFile = FileUtils.ASCIIDataWrite()
#myOutFile = FileUtils.BinDataWrite()
# start with new datafile (note "1" at end)
myOutFile.openOutput('',fName,1)



###############################################################################
# add info strings to record file
###############################################################################
# create the file header , with information about the recording
infostr = len(header) * "#" + "\n"
infostr = infostr + "[aqdata]" + "\n"
infostr = infostr + "#date\t:\t\t" + str(TimeUtils.getTS()) + "\n"
for info in aqdata:
    infostr = infostr + str(info) + "\t: " + "\t\t" + str(aqdata[info]) + "\n"

infostr = infostr + (len(header) * "#") + "\n" + "\n"

infostr = infostr + "[communication]" + "\n"
for info in com:
    infostr = infostr + str(info) + ": " + "" + str(com[info]) + "\n"

infostr = infostr + (len(header) * "#") + "\n" + "\n"

infostr = infostr + "[misc]" + "\n"
for info in misc:
    infostr = infostr + str(info) + ": " + str(misc[info]) + "\n"

infostr = infostr + (len(header) * "#") + "\n" + "\n"

infostr = infostr + "[trigger]" + "\n"
for info in trigger:
    infostr = infostr + str(info) + ": " + str(trigger[info]) + "\n"

infostr = infostr + (len(header) * "#") + "\n" + "\n"

infostr = infostr + "[debug]" + "\n"
for info in dbg:
    infostr = infostr + str(info) + ": " + str(dbg[info]) + "\n"

infostr = infostr + (len(header) * "#") + "\n" + "\n"

infostr = infostr + "[values]" + "\n"
for info in value:
    infostr = infostr + str(info) + ": " + str(value[info]) + "\n"

unitstr = ""
hdrname = str(header).split(";")

for info in hdrname:
    # create the units here:
    valname = str(info).split("[")
    unit = ""
    if len(valname) > 1:
        unit = "[" + valname[1]
    unitstr = unitstr + unit + misc["delimiter"]
unitstr = unitstr[:-1]
infostr = infostr + (len(header) * "#") + "\n" + "\n"
myOutFile.writeStr(infostr,0, 0)
myOutFile.writeStr(header,0, 0)
myOutFile.writeStr(unitstr,0, 0)
myOutFile.closeOutput()

#copy datafile to header file, for header of further datafiles

hfile = misc["datafileprefix"] + '_header.csv'
shutil.copyfile(fName, hfile)

# open datafile for append (note "0" at end)
myOutFile.openOutput('',fName,0)

# set run condition for no exit, first run before exit ;-)
exitprg = False
# check for autostart
if int(misc["autostart"])==1:
    pause = False
else:
    pause = True
    
# use cross-platform kbhit for keyboard detection
kb = KBHit()

numfile = 0
trgfile = numfile

# define the runtime timer
runtime = TimeUtils.Timer()
totaltime = TimeUtils.Timer()

#display how to stop the program

# always allow manual trigger...
#  do_trigger:
#     print 'ESC - Exit program\nP - Pause\nS - Start\nT - Trigger new file\n\n number of scans:\n'
# else:
#     print 'ESC - Exit program\nP - Pause\nS - Start\n\nnumber of scans:\n'
os.system('cls' if os.name == 'nt' else 'clear')
if not demo:
    print '\n***************** Aqserver running using config file: *****************'
    print '\n%s\n\n' % configfile
    print 'ESC - Exit program\nP - Pause\nS - Start\nT - Trigger new file\n\nNumber of scans:\n'
else:
    print '\n*********** Aqserver running in DEMO mode using config file: ***********'
    print '\n%s\n\n'  % configfile
    print 'ESC - Exit program\nP - Pause\nS - Start\nT - Trigger new file\n\nNumber of scans:\n'

###############################################################################
# get prepared to scan    
###############################################################################

# outer loop, exit only with exitprg

while not exitprg:

    # preset some parameters before we start to scan
    # record counter
    numrec=0
    num_posttrg_recs = numrec + 5

    # reset the timer
    runtime1 = runtime.Reset()
    
    # reset manual trigger
    man_trigger = True

        

    ###############################################################################
    # now start the scan loop
    ###############################################################################
    # run the loop as long as no trigger event has occured 
    # or the number of actual records is smaller than number of post trigger limit
    # or when we will have no trigger

    while (not triggered or (numrec < num_posttrg_recs) or (not do_trigger and not man_trigger) or (trgfile != numfile)) and not exitprg and (numrec < maxrecords):
    
        prnrem = numrec % 10
        if (prnrem == 1):
#            runtime1 = runtime.GetTotal()
#            totaltime1 = totaltime.GetTotal()
#            fitime = str(datetime.timedelta(seconds=runtime1))
#            totime = str(datetime.timedelta(seconds=totaltime1))
#            timestr = " file time: %s,  total time: %s" %(fitime, totime)
            # print loop number, so we see program is active, always in same line!
#            printme = str("scans: " + str(numrec - 1) + " files: " + str(numfile + 1)  + timestr)
            printme = str("scans: " + str(numrec - 1) + " files: " + str(numfile + 1))
            digits = len(printme)
            # get number of backspaces to start printing at 1st column
            delete = "\b" * (digits + 1)
            # always print in same line
            print "\r{0}{1:{2}}".format(delete, printme, digits),
        
        # use interval for recording (sleep for x seconds)
        
        if (int(misc["scantime"]) > 0) or demo:
            sleep(scantime)
        
        # check if recording is paused 
        # Tip: can be recognized when loop number is not counting
        if not pause:
            
            
            # increase record counter
            numrec += 1
            fnum = ""
            # now loop through our calls, (multivar only 20 variables per call!)
            for y in range(calls): 
                data_items = lvariables[y]
                formats = lformats[y]
                names = lnames[y]
            
                # create buffers to receive the data
                # use the Amount attribute on each item to size the buffer
                for di in data_items:
                    # create the buffer
                    buffer = ctypes.create_string_buffer(di.Amount)

                    # cast the pointer to the buffer to the required type
                    pBuffer = ctypes.cast(ctypes.pointer(buffer),
                                          ctypes.POINTER(ctypes.c_uint8))
                    di.pData = pBuffer
                    
                if not demo:
                    # reset connection attempts, when connected
                    if clientConnected:
                        attempts = 0
                else:
                    attempts = 0

                # now do the read_multi_vars
                try:
                    # check for demo
                    if not demo:
                        # connect, if not already connected (after error)
                        if not clientConnected:
                            print "\nnot connected, %d attempts" %attempts
                            if doError:
                                logentry = "reconnecting client"
                                logger.info(" %s: %s" %(TimeUtils.getTS(), logentry))
                            client.connect(IP,RACK,SLOT)
                            clientConnected = True
                        result, data_items = client.read_multi_vars(data_items)
                        
                        for di in lvariables[y]:
                            check_error(di.Result)

                except:
                    # disconnect on error
                    attempts += 1
                    if clientConnected:
                        if doError:
                            logentry = "disconnecting client, because of raised exception"
                            logger.error(" %s: %s" %(TimeUtils.getTS(), logentry))
                        client.disconnect()
                        clientConnected = False
                        numrec -= 1
                    pass

                else: # ..try .. except .. else
                    # unpack and print the result of each read
                    for i in range(0, len(data_items)):
                        fmt = formats[i]
                        nm = names[i]
                        di = data_items[i]
                        myByteStr =""
                        if not demo:
                            myBytes = ''.join([chr(di.pData[i]) for i in range(0, di.Amount)])
                        else:
                            if fmt == '>B':
                                # create boolean byte format
                                myBytes = struct.pack(fmt,random.randint(0, 255))
                            elif fmt == '>b':
                                # create byte as integer
                                myBytes = struct.pack(fmt,random.randint(-128, 127))
                            elif fmt == '>h':
                                # create random word
                                myBytes = struct.pack(fmt,random.randint(-32767, 32767))
                            elif fmt == '>i':
                                # create double word
                                myBytes = struct.pack(fmt,random.randint(-16777216, 16777216))
                            elif fmt == '>f':
                                # create float
                                myBytes = struct.pack(fmt,random.uniform(-16777216, 16777216))
                            

                        # Handle boolean variables
                        if fmt == '>B':
                            # get the values of the byte as integer
                            mbyte = int(struct.unpack(fmt, myBytes)[0])
                            # get the bit names
                            bitname = nm.split(',')
                            offset = 0
                            for j in range(0,len(bitname)):
                                # check value of lowest bit
                                if bool(mbyte & 1):
                                    # check if there is a name for the bit (name NOT empty)
                                    if bitname[j] != "":
                                        bitval = 1 + offset
                                        if booloff:
                                            myByteStr = myByteStr + str(bitval) + misc["delimiter"]
                                            offset += 2
                                        else:
                                            # if so, append value 1 to the string
                                            myByteStr = myByteStr + "1" + misc["delimiter"]
                                else:
                                    # check if there is a name for the bit (name NOT empty)
                                    if bitname[j] != "":
                                        bitval = offset
                                        if booloff:
                                            myByteStr = myByteStr + str(bitval) + misc["delimiter"]
                                            offset += 2
                                        else:
                                            # if so, append value 0 to the string
                                            myByteStr = myByteStr + "0" + misc["delimiter"]
                                # shift byte to the right for next bit
                                mbyte = mbyte >> 1
                        else:
                            myByteStr = str(struct.unpack(fmt, myBytes)[0])  + misc["delimiter"]

                        fnum = fnum + myByteStr
                        
                        # check the trigger condition
                        if do_trigger and nm == str(trigger["trgsignal"]) and not triggered:
                            trgsignal = float(str(struct.unpack(fmt, myBytes)[0]))
                            if eval(trgexpression):
                                triggered = True
                                if postrec > 0:
                                    num_posttrg_recs = numrec + postrec
                                    if doInfo:
                                        logentry = 'value trigger !! Waiting for post-trigger records'
                                        logger.info(" %s: %s" %(TimeUtils.getTS(), logentry))
                                else:
                                    num_posttrg_recs = numrec
                                    if doInfo:
                                        logentry = 'value trigger !! No post-trigger records'
                                        logger.info(" %s: %s" %(TimeUtils.getTS(), logentry))
                        elif (do_trigger and nm == str(trigger["trgsignal"]) and triggered and (trgfile != numfile)) or man_trigger:  
                            trgsignal = float(str(struct.unpack(fmt, myBytes)[0]))
                            if not eval(trgexpression) and not man_trigger:
                                triggered = False
                                num_posttrg_recs = numrec + 1
                                trgfile = numfile
                        # increase comparison value for post-trigger end condition
                        # so we do not end, when not yet triggered
                        if not triggered:
                            num_posttrg_recs = numrec + 1
                        
                    # write record after we have read all values
                if not demo:
                    if not clientConnected:
                        break
            
            myOutFile.writeStr(fnum, misc["delimiter"], 1, 1)
            
        # check for ESC key to end recording and further keys...

        if kb.kbhit():
            pressedKey = ord(kb.getch())
            # check for keyboard EXIT
            if pressedKey == 27 or (attempts >= maxattempts and maxattempts !=0):    # 27 = ESC
                exitprg = True
            # check for keyboard PAUSE
            if pressedKey == 112 or pressedKey == 80:    # 112 = p, 80 = P
                pause = True
            # check for keyboard START
            if pressedKey == 115 or pressedKey == 83: # 115 = s, 83 = S
                pause = False
            # check for keyboard TRIGGER
            if pressedKey == 116 or pressedKey == 84 and not triggered: # 116 = t, 84 = T
                triggered = True
                num_posttrg_recs = numrec
                man_trigger = True
                if doInfo:
                    logentry = 'Keyboard trigger !!'
                    logger.info(" %s: %s" %(TimeUtils.getTS(), logentry))
                
    # end of while loop for scanning (ended with trigger or exitprg)
    print ('\n')            
    runtime1 = runtime.GetTotal()
    totaltime1 = totaltime.GetTotal()

    if doInfo:
        if numrec > 0:
            logentry = str(numrec) + ' values, file runtime: ' + str(runtime1) +' [s], average: ' + str(runtime1 / numrec) 
            logger.info(" %s: %s" %(TimeUtils.getTS(), logentry))


    # close file
    myOutFile.closeOutput()
    
    # define files
    # first we have to make the correct path, replace \ with \/
    datapath = str(misc["datapath"])
    datapath = datapath.replace("\\","\/\/")

    # check path
    if os.path.exists(datapath):
        if usedir:
            year, month, day = TimeUtils.getYMD()
            datapath = datapath + year + "\/"
            if not os.path.exists(datapath):
                os.mkdir(datapath)
            datapath = datapath + month + "\/"
            if not os.path.exists(datapath):
                os.mkdir(datapath)
            datapath = datapath + day + "\/"
            if not os.path.exists(datapath):
                os.mkdir(datapath)
        fNameComp = datapath + misc["datafileprefix"]
        if doDebug:
            logentry = "file name : " + str(fName)
            logger.debug(" %s: %s" %(TimeUtils.getTS(), logentry))
            logentry = "compressed file name : " + str(fNameComp)
            logger.debug(" %s: %s" %(TimeUtils.getTS(), logentry))
    else:
        print "path does not exist: %s" %str(misc["datapath"])
        print "using %s\/ instead!" %MyDataDir
        if doWarning:
            logentry = "path does not exist: " + datapath
            logger.warning(" %s: %s" %(TimeUtils.getTS(), logentry))
        datapath = MyDataDir + "\/"
        if usedir:
            year, month, day = TimeUtils.getYMD()
            datapath = datapath + year + "\/"
            if not os.path.exists(datapath):
                os.mkdir(datapath)
            datapath = datapath + month + "\/"
            if not os.path.exists(datapath):
                os.mkdir(datapath)
            datapath = datapath + day + "\/"
            if not os.path.exists(datapath):
                os.mkdir(datapath)
        fName = str(MyDataDir + "\/" + misc["datafile"] + ".csv")
        fName2 = str(MyDataDir + "\/" + "finished.csv")
        fNameComp = str(datapath + "\/" + misc["datafileprefix"])


    inFile = fName
    outFile = fNameComp + TimeUtils.getTSfName() + ".csv" + '.gz'

    # save current recording as compressed file with timestamp in filename
    FileUtils.compressFile(inFile,outFile)
    if doInfo:
        logentry = 'created archive: ' + outFile 
        logger.info(" %s: %s" %(TimeUtils.getTS(), logentry))
#     print 'created archive: %s\n' % outFile

    if not exitprg and (triggered or numrec >= maxrecords):
        tempfile1 = misc["datafileprefix"] + '_temp1.csv'
        tempfile2 = misc["datafileprefix"] + '_temp2.csv'
        tempfile3 = misc["datafileprefix"] + '_temp3.csv'
        headerfile = misc["datafileprefix"] + '_header.csv'
        os.system('cls' if os.name == 'nt' else 'clear')
        if not demo:
            print '\n***************** Aqserver running using config file: *****************'
            print '\n%s\n\n' % configfile
            print 'ESC - Exit program\nP - Pause\nS - Start\nT - Trigger new file\n\nNumber of scans:\n'
        else:
            print '\n*********** Aqserver running in DEMO mode using config file: ***********'
            print '\n%s\n\n'  % configfile
            print 'ESC - Exit program\nP - Pause\nS - Start\nT - Trigger new file\n\nNumber of scans:\n'

        # print '\nESC - Exit program\nP - Pause\nS - Start\nT - Trigger new file\n\n number of scans:\n'
        # copy the pre-trigger and posttrigger records to new file
        PrgUtils.fileCopyTrgLines(fName, tempfile1, copyrec)
        # reorder the record numbers, starting from 1
        PrgUtils.fileReOrder(tempfile1, tempfile2, misc["delimiter"], True)
        # remove old datafile
        # os.remove(fName)
        # make the new datafile
        PrgUtils.fileAppend(tempfile3,headerfile,tempfile2,False,True)
        # open datafile for append (note "0" at end)
        shutil.copy2(tempfile3,fName)
        myOutFile.openOutput('',fName,0, copyrec)
        numfile += 1
        man_trigger = False
        triggered = False
        num_posttrg_recs = numrec + 1
        trgfile = numfile

            
# end of while loop, with exitprg
    

if not demo:
    #disconnect PLC
    client.disconnect()
    client.destroy()

# delete temporary files
tempfile3 = misc["datafileprefix"] + '_temp3.csv'
headerfile = misc["datafileprefix"] + '_header.csv'
if os.path.isfile(headerfile):
    os.remove(headerfile)
if os.path.isfile(tempfile3):
    os.remove(tempfile3)

#always log program end
logger.setLevel(logging.INFO)
logentry = "################## program stopped by user ###################"
logger.info(" %s: %s" %(TimeUtils.getTS(), logentry))
    
print "Good bye from aqserver..."

