Installation
============

Program can be obtained from http://www.taxis-instruments.de .

The program was written using Python 2.7.10 under Windows 7 - 32 bit.

Install from source
___________________

If you would like to run from the python source you must have a working Python 2.7 installation. For a full working Python environment I can recommend the Python (x,y) distribution from https://python-xy.github.io/ or Winpython from https://winpython.github.io/ for a Windows environment (just make sure you are using the latest Python 2 package). On Linux and MacOS environments Python should already be installed as part of the OS.

Program is using (at least parts of) the following Python libraries (not in any particular order..):

* time
* sys
* os
* shutil
* ctypes
* struct
* logging
* collections
* win32com
* python-snap7
* socket
* datetime
* gzip
* bz2
* binascii
* ConfigParser
* distutils

This libraries can be installed with pip.

Python-snap7 is a python wrapper for snap7 from http://snap7.sourceforge.net/. So make sure you have a working copy of this also on your machine.

Install with Windows Installer
_________________________________

To install the program you can use the provided installer. Run setup.exe as Administrator and follow instructions of the installer. A link to the program will be installed into the startmenu.
The program will be installed to the directory "C:\\Program Files (x86)\\Aqserver\\". Additionally the folder "Aqserver" plus sub folders "help", "log" and "data" will be created in the My Documents folder of the current user.
In the "Aqserver" directory you will find the following files:

* test.bat: a Windows / DOS batch file that will start Aqserver with the test configuration. You can copy and edit this file to personalize it for different configuration. I am also using this to start Aqserver from Windows Explorer or to run multiple instances (one batch file per instance)
* test.cfg: an example config file that you can edit to match your requirements (good idea is to make a copy first..)


To uninstall run the uninstaller from the startmenu or uninstall from windows control panel.

Manual installation
_______________________

To install the program in a Windows Environment without a working Python installation use a folder of your liking and copy the files aqserver.exe, aqserver.cfg, aqserver.chm and aqserver.pdf to this folder. Copy snap7.dll to your Windows\\system32 directory. That's all. No install or setup procedure.
To remove the program just delete these files from your system. Nothing will remain.
