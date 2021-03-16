Command line options
=====================
Acqserver's  command line options are the following:
(type 'python aqserver.py --help' to show the text below)


.. code:: text

    >python aqserver.py --help
    usage: aqserver.py [-h] [-c CONFIG]

    Siemens S7 data acquisition server

    optional arguments:
      -h, --help            show this help message and exit
      -c CONFIG, --config CONFIG
                            specify name of configfile, defaults to aqserver.cfg

    This program was written using the python-snap7 module and the snap7 library.
    A configfile must exist (default file is aqserver.cfg) that defines
    communication and other parameters and of course the S7 variables to scan.
    Open this file in your preferred editor and read the comments on how to
    configure.
    Values will be stored to csv-file in subdirectory data. Filename can be
    specified in configfile. Once a configurable trigger is raised, a new datafile
    begins.
    After trigger or when program is stopped, the data file will be compressed and
    stored to a path, that can also be specified in the config file.
