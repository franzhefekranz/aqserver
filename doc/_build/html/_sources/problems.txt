Problems
===========

When program exits unexspected or with a message, or when program crashes, then you should turn on debugging. By default debugging is off. To run the program with debugging enabled open your config file and set 
configuration value "dbglevel" to a value >0. (See below). 1 for INFO is the most verbose level. If you face problems / errors set at least to 3.

.. code:: text

	###############################################################################
	# debug settings
	###############################################################################
	[debug]

	# debug level
	# set logging level to debug, write program actions
	# to logfile
	# 0 - no logging
	# 1 - log INFO messages (default setting)
	# 2 - log WARNING messages
	# 3 - log DEBUG messages
	# 4 - log ERROR messages
	# 5 - log CRITICAL messages
	# 6 - log EXCEPTION messages
	dbglevel = 0 
	
Then you should start the program again and after program has ended (again) you should check the log file in the sub directory log. There you should find some more detailed information why the program won't run.
Adjust (probably) your configuration and try to run again.

Problems can be caused by:

* PLC cannot be reached with communication parameters provided
* value in your list does not exist in PLC
* typo in configuration values

If you still can't manage to make it run, send a copy of your logfile and the config file to my mail address (aqserver at taxis-instruments dot de). 

Frequently asked questions
--------------------------

None so far. This will be updated as questions arise. Post your questions in the contact form on my homepage or send mail to  <aqserver at taxis-instruments dot de>