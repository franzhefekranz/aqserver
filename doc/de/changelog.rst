Changelog
=========
V0.3
15 October 2020

* aqserver.py: enhancement for config file. Added gain, offset and unit for all values. Former unit in name is skipped.
* aqserver.py: separated header file from datafile, when saving /compressing. Datafile is saved and compressed with every trigger event (manual / configured / max. number of values). Header file is saved on program exit only, with timestamp. Now we can use same *.kst file when changing number of parameters in config-file. But do only append new values, so we don't change order of existing values!
* aqserver.py: added console progress bar
* updated and enhanced documentation
* renamed install file to Aqserver-x.x.x.exe where x.x.x is program version, e.g. Aqserver-0.3.exe
* updated demo config file with docs about gain, offset and unit

V0.2
28 March 2017

* aqserver.py: added writing units for values to datafile 
* aqserver.py: added functionality for demo: creating data from ramdom function, without connection to plc. DEMO is shown in headline of aqserver
* aqserver.py: added functionality for booloffset: boolean values within one byte are added an offset, so they can be shown in one plot without overlapping each other
* PrgUtils.py: added config.optionxform=str tor get_config for case sensitive config values. ATTENTION: config values IP, RACK and SLOT must be changed to lowercase in your new config files (ip, rack,slot)

V0.1.15
17 March 2017

* aqserver.py: added config filename to display, so we know what is running
* aqserver.py: delete header file and temp files when program exits

V0.1.14
15 March 2017

* aqserver.py: fixed error: when using multiple instances still same name for header file (and temp file) was used. This messed up data files. Now included datafileprefix in these filenames so they are unique.
* aqserver.py: for same reason logfile name was abandoned, using datafileprefix instead to have unique name

V0.1.13
13 February 2017

* added german docs

V0.1.12
13 October 2016

* updated docs
* created new installer using pyinstaller and NSIS. Problems before with py2exe.

11 OctoV0.1.11
ber 2016

* added check for maximum records (from config) to avoid files getting too big
* added try ..except for reading config file

V0.1.10
06 October 2016

* PrgUtils.py: added get username for all OS (Windows, Linux, MacOS)
* aqserver.py: change data and log directory, depending on OS. In Windows this will be sub directories of .. My Documents\\Aqserver folder, in Linux/MacOS this will be in current users home directory (//home//user//Aqserver//..)

V0.1.9
05 October 2016
 
* NSIS: tried to make setup.exe for Windows
* aqserver.py: added manual trigger always possible
* aqserver.py: added check for variables, and exit with config fault, problem to logfile

V0.1.8
30 September 2016
 
* updating docs
* aqserver.py: check if argument for config file is list or string
* aqserver.py: added purging log directory, when debug is 0 (= no debugging), only actual logfile remains, with entry program start and end
* aqserver.py: improved error detection, connect and disconnect of client

V0.1.7
29 September 2016
 
* updated docs
* compiled to exe with py2exe
* can test now with local Snap7 server
* added verification for configfile, data dir and log dir, if a dir is missing it will be created
* fixed keypress problem, program was not responding to every keypress

V0.1.6
15 September 2016

* added try..except for communication error, program exits normal now, with message to user and logfile
* when client was already connected program tries to disconnect and to connect again (no exit)
* when scantime is set to 0 then program scans as fast as possible (no sleep)

V0.1.5
28 November 2015

* modified aqserver(none OOP version), can now use directory structure year\month\day  for saved files

V0.1.4
11 August 2015 

* started refactoring and making OOP aware, with acqserver class (not yet finished)

V0.1.3
10 August 2015 

* tested and corrected trigger functionality
* tested S7 300 with plcsim and nettoplcsim

V0.1.2
07 August 2015 

* added filecopy routines to PrgUtils
* added trigger functionality to server (aqserver.py)

V0.1.1
06 August 2015 

* added config section for debug, with settings for debug level, logfile
* corrected error in endless loop that creates string with values
* create header template at start, that can be copied to further data files in case of trigger
* removed all sys.args, only*c configfile remains, all other settings in config file
* tried to start 2 instances of program

 * use different configfile
 * set different recording filename
 * when started from 2 cmd environments with*c parameter and different configfile, it works!
 
* tested filecopy, rename, append, replace in file as preparation for trigger event actions

V0.1
05 August 2015 

* added data file name to config, so we can start aqserver several times using different settings, when scanning several PLCs
