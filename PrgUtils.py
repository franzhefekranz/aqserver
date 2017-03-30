# - *-  coding: utf- 8 - *-
from argparse import ArgumentParser, RawTextHelpFormatter
import ConfigParser
import collections
from collections import deque
import os
import shutil
# Windows
if os.name == 'nt':
    import win32api
    import win32security
    import win32profile
# Posix (Linux, OS X)
else:
    import pwd

def parse_sys_args():
    """
    ###############################################################################
    # parse sys arguments
    # -h help
    # -c name of config file 
    ###############################################################################
    """
    parser = ArgumentParser(description='Siemens S7-400 data acquisition server',
             formatter_class=RawTextHelpFormatter,
            epilog = '''This program was written using the python-snap7 module
and the snap7 library.
A configfile must exist (default file is aqserver.cfg) that defines
communication and other parameters and of course the S7 variables to scan.
Open this file in your preferred editor and read the comments on how to
configure.
Values will be stored to csv-file in subdirectory data. Filename can be 
specified in configfile. Once a configurable trigger is raise, a new datafile
begins. 
After trigger or when program is stopped, the data file will be compressed and 
stored to a path, that can also be specified in the config file.         
''')
    parser.add_argument("-c", "--config", type = str, nargs = 1, default = "aqserver.cfg",
                        help="specify name of configfile, defaults to aqserver.cfg")
    args = parser.parse_args()
    cfg = args.config
    # print cfg
    return cfg
    
def get_config(cfgfile):
    """
    ###############################################################################
    # read configuration from file
    ###############################################################################
    """
#    config = ConfigParser.RawConfigParser()
    config = ConfigParser.ConfigParser()
    config.optionxform=str
    config.read(cfgfile)

    ###############################################################################
    # define the sections
    ###############################################################################
    acquisition = config.items('aqdata')
    communication = config.items('communication')
    miscellaneous = config.items('misc')
    values = config.items('values')
    triggers = config.items('trigger')
    debug = config.items('debug')

    ###############################################################################
    # put values in dict per section
    ###############################################################################
    aqdata = collections.OrderedDict(acquisition)
    com = collections.OrderedDict(communication)
    misc = collections.OrderedDict(miscellaneous)
    value = collections.OrderedDict(values)
    trigger = collections.OrderedDict(triggers)
    dbg = collections.OrderedDict(debug)
    
    return aqdata, com, misc, value, trigger, dbg
 
def fileCopyTrgLines(infile, outfile, numlines):
    """
    ###############################################################################
    # copies the 'overlapping' lines from old to ne data file after a trigger event
    # lines number will be rewritten starting with 1
    ###############################################################################
    """
    with open(infile) as fin, open(outfile, 'w') as fout:
        fout.writelines(deque(fin, numlines))
        
def fileReOrder(infile, outfile, delimiter, del1 = False):
    with open(infile) as fin, open(outfile, 'w') as fout:
        x=1
        for line in fin:
            parts = line.split(delimiter)
            parts[0] = str(x)
            line = delimiter.join(parts)
            fout.writelines(line)
            x += 1
    if del1:
        os.remove(infile)
            
def fileAppend(dest,src1,src2,del1=False,del2=False):
    """
    ###############################################################################
    # appends two files 'src1' and 'src2' and writes to file 'dest'
    # if 'del1' is True, then file 'src1', will be deleted after append operation,
    # same with 'del2' and 'src2'
    ###############################################################################
    """
    
    outfile=dest

    destination = open(outfile,'wb')
    shutil.copyfileobj(open(src1,'rb'), destination)
    shutil.copyfileobj(open(src2,'rb'), destination)
    destination.close()        
    
    if del1:
        os.remove(src1)
        
    if del2:
        os.remove(src2)
        


# def get_username():
#    """
#        ###############################################################################
#    # returns the username
#    ###############################################################################
#    """
#    if os.name == 'nt':
#        return win32api.GetUserName()
#    else:
#        return pwd.getpwuid( os.getuid() )[ 0 ]        

        

    



