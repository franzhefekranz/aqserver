Usage
=====

Starting from a python console
------------------------------

In a python console program can be started with:

.. code:: text

    >python aqserver.py

or

.. code:: text

    >aqserver.py

Starting the program without any consecutive arguments, will assume that you will use the default config file name "aqserver.cfg".

It is a good idea to keep a config file for every installation you use to record data. So in this case when not using the default config file you start with:

.. code:: text

    >aqserver.py -c my3rd.cfg

or whatever name you give your config file. It is good practice to always use the extension ".cfg" but  it will also work without it. Just make sure you always use the complete filename including any extension.

.. image:: images/usage1.png
    :align: center
    :alt: Console showing Aqserver in run	

As you can see in the picture above, the program is displaying some options plus the number of scans in the current data file and the number of data files recorded so far.
The options that you can use are as follows:

* ESC - Exit program : When you hit the "ESC" key the current file will be saved and then the program stops.
* P - Pause: recording can be paused with the "p" key, meaning nothing will be read from the PLC and nothing will be written to the file. This can be useful if you have a break in production, but you still want the file to be continued.
* S - Start: When program was paused or when config item autostart  is set to 0 then you can start/continue recording with  key 'S".
* T - Trigger new file: With the "t" key you can manually raise a trigger. The actual data file will be stored and a new file will be started, indicated by the increasing number of files. Also number of scans start with 1 again.

Using Windows installer version
-------------------------------

When you have installed Aqserver using the Windows installer, then usage is slightly different. You also might not have a working python environment installed. The installer installs the aqserver exe to  the directory "C:\\Program Files (x86)\\Aqserver\\". An example config file and a Windows / DOS batch file is copied to the "..\\My Documents\\Aqserver\\" directory. Once you have defined your config file you should edit a copy of the batch file accordingly, so that aqserver will be started using your new config file.
Contents of the batch file:

.. code:: text

    "C:\Program Files (x86)\Aqserver\aqserver.exe" -c "path_to\test.cfg"
    pause


Change path and name of your config file. Then Aqserver can be started with double clicking the batch file in Windows Explorer.

