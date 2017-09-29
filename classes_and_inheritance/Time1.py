"""

Code example from Think Python, by Allen B. Downey.
Available from http://thinkpython.com

Copyright 2012 Allen B. Downey.
Distributed under the GNU General Public License at gnu.org/licenses/gpl.html.

"""

class Time(object):
    """Represents the time of day.
       
    attributes: hour, minute, second
    """

    def __init__(self, hour = 0, minute = 0, second = 0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def __add__(self, other):
        seconds = self.time_to_int(self) + other.time_to_int(other)
        return self.int_to_time(seconds)


    def __str__(self):
        return '%.2d:%.2d:%.2d' % (self.hour,self.minute,self.second)

    def print_time(self,time):
        print '%.2d:%.2d:%.2d' % (time.hour, time.minute, time.second)


    def int_to_time(self,seconds):
        """Makes a new Time object.

        seconds: int seconds since midnight.
        """
        time = Time()
        minutes, time.second = divmod(seconds, 60)
        hour, time.minute = divmod(minutes, 60)
        day, time.hour = divmod(hour, 24)
        return time


    def time_to_int(self,time):
        """Computes the number of seconds since midnight.

        time: Time object.
        """
        minutes = time.hour * 60 + time.minute
        seconds = minutes * 60 + time.second
        return seconds


    def add_times(self,t1, t2):
        """Adds two time objects."""
        assert self.valid_time(t1) and self.valid_time(t2)
        seconds = self.time_to_int(t1) + self.time_to_int(t2)
        return self.int_to_time(seconds)


    def valid_time(self,time):
        """Checks whether a Time object satisfies the invariants."""
        if time.hour < 0 or time.minute < 0 or time.second < 0:
            return False
        if time.minute >= 60 or time.second >= 60:
            return time
        return True


    def main(self):
        # if a movie starts at noon...
        noon_time = Time()
        noon_time.hour = 12
        noon_time.minute = 0
        noon_time.second = 0

        print 'Starts at',
        self.print_time(noon_time)

        # and the run time of the movie is 109 minutes...
        movie_minutes = 109
        run_time = self.int_to_time(movie_minutes * 60)
        print 'Run time',
        self.print_time(run_time)

        # what time does the movie end?
        end_time = self.add_times(noon_time, run_time)
        print 'Ends at',
        self.print_time(end_time)



if __name__ == '__main__':
    time = Time()
    time.main()
