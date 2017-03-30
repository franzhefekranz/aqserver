#-------------------------------------------------------------------------------
# Timestamp and Execution Timer Utilites
#-------------------------------------------------------------------------------
# Contains a timestamp function and an execution timer class.
# 
# The function getTS() returns a timestamp as an ASCII string. The class Timer
# defines a timer object that is suitable for capturing things like code
# execution times or I/O latency times.
#-------------------------------------------------------------------------------
# Example source code for the book "Real-World Instrumentation with Python"
# by J. M. Hughes, published by O'Reilly Media, December 2010,
# ISBN 978-0-596-80956-0.
#-------------------------------------------------------------------------------
import  datetime
import  time

def getTS():
    """ Get current date and time from the system.

        Format the data and time into a string and return it to the caller. The
        data is in YYYY-MM-DD format, and the time is in HH:MM:SS.MS format.
		e.g. for timestamp: 2015-04-09 11:01:19.355
    """
    # fetch the current data and time from the system. Note that currutime
    # is not used, but it's there if you need it.
    t = datetime.datetime.now()
    currdatetime = t.timetuple()
    # currutime = time.mktime(t.timetuple())

    # extract the values of interest from the string generated by time.mktime()
    # yr = str(currdatetime[0])
    curr_date = "%04d-"%currdatetime[0] + "%02d-"%currdatetime[1] + "%02d"%currdatetime[2]
    curr_time = "%02d:"%currdatetime[3] + "%02d:"%currdatetime[4] + "%02d."%currdatetime[5] + "%03d"% int(t.microsecond//1000)

    return (curr_date + " " + curr_time)

def getTSfName():
    """ Get current date and time from the system.

        Format the data and time into a string and return it to the caller. The
        data is in YYYY-MM-DD format, and the time is in HH:MM:SS.MS format.
		e.g. for timestamp: 2015-04-09 11:01:19.355
    """
    # fetch the current data and time from the system. Note that currutime
    # is not used, but it's there if you need it.
    t = datetime.datetime.now()
    currdatetime = t.timetuple()
    # currutime = time.mktime(t.timetuple())

    # extract the values of interest from the string generated by time.mktime()
    # yr = str(currdatetime[0])
    curr_date = "%04d"%currdatetime[0] + "%02d"%currdatetime[1] + "%02d"%currdatetime[2]
    curr_time = "%02d"%currdatetime[3] + "%02d"%currdatetime[4] + "%02d"%currdatetime[5]

    return (curr_date + "_" + curr_time)

def getYMD():
	""" Get current date and time from the system.
		
		Format the data and time into a string and return it to the caller. The
		data is in YYYY-MM-DD format, and the time is in HH:MM:SS.MS format.
		e.g. for timestamp: 2015-04-09 11:01:19.355
	"""
	# fetch the current data and time from the system. Note that currutime
	# is not used, but it's there if you need it.
	t = datetime.datetime.now()
	currdatetime = t.timetuple()
	# currutime = time.mktime(t.timetuple())
	
	# extract the values of interest from the string generated by time.mktime()
	# yr = str(currdatetime[0])
	year = "%04d"%currdatetime[0]
	month = "%02d"%currdatetime[1]
	day = "%02d"%currdatetime[2]
	
	return (year, month, day)

class Timer:
    """ General purpose timer class.

        Useful for creating multiple instances of a timer suitable for
        capturing code execution times. Object instantiations of Timer will
        not collide with one another and share no data between each instance.

        All time values are returned in fractional seconds as floating point
        values.
    """
    def __init__(self):
        self.tstart = 0
        self.tlast  = 0
        self.tcurr  = 0

        self.Reset()


    def GetDelta(self):
        """ Returns time since last call to GetDelta()

            Essentially just a "lap" timer. Does not modify or clear the
            running time. Updates the local attributes tcurr and tlast.
        """
        self.tcurr = time.clock()
        delta = self.tcurr - self.tlast
        self.tlast = self.tcurr
        return delta


    def GetTotal(self):
        """ Returms time since timer object created.
        """
        return time.clock() - self.tstart


    def Reset(self):
        """ Initialize time attributes.

            Sets local data atributes tstart and tlast to the current
            system time.
        """
        self.tstart = time.clock()
        self.tlast = self.tstart