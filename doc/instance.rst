Running multiple instances
==========================

If you have 2 (or more..) PLCs you want to monitor, you can do so, by running 2 separate
instances of aqserver:

Create a second config-file, containing the data required for the second connection.

.. note:: Make sure you use a datafile name that is different to the other instance(s).

* use a different name for the config-file
* in the config-file set a different datafile name
* start acqserver from the commandline, using the -c option
* e.g. in Windows run:

.. code:: text

    >python aqserver.py -c my_new_config_file.cfg
	
If you have installed Aqserver with the provided Windows installer, you can use the batch file(s) in your "..\\My Documents\\Aqserver\\" folder to start the program. (See also "Installation" section of this manual). For every instance create a batch file that contains the correct settings for the used config file.
