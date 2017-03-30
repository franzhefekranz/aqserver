Aqserver
========

With this program you can record values from a Simatic S7 PLC to a CSV File. Depending on the number of values to record the scan time is changing, thus increasing with the number of values. It is possible to set trigger conditions, that will start a new file. The old file will be compressed and stored in a selectable directory tree.
Using a pre- and post trigger time, you can set an overlap of old and new file. If you are not able to set a working trigger, the trigger can also be activated manually.

A config file must exist (default file is aqserver.cfg) that defines communication and other parameters and of course the S7 variables to scan. Open the config file in your preferred editor and read the comments on how to
configure.

Values will be stored to a csv-file in subdirectory data. Filename can be specified in configfile. Once a configurable trigger is raised, a new datafile begins.

After trigger or when program is stopped, the data file will be compressed and stored to a path, that can also be specified in the config file.

When running several instances of the program, using different config files, values can be recorded from different PLCs at the same time.

Please note that this program is in an early stage of development. If you run into problems when using it, see the "Problems" section of this manual. Aqserver will not create a problem with your PLC program though.

Using Kst2 from https://kst-plot.kde.org the datafile can be read and plotted online during the recording. Also decompressed archives can be plotted to your liking.

An alternative would be LiveGraph from http://www.live-graph.org , but then the data files must be modified, because LiveGraph is expecting csv-files in a certain format (actually this is not provided by Aqserver at the moment).

