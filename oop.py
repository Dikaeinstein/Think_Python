class Time:
    """Represents the time of day.
    
    attributes: hour, minute, second.
    """
    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second
        
    def __str__(self):
        """String representation of Time object in the form h:m:s.
        
        self: Time object.
        """
        return "{0:02.0f}:{1:02.0f}:{2:02.0f}".format(self.hour, self.minute, self.second)
    
    def __add__(self, other):
        """Performs "+" operation on Time objects.
        """
        if isinstance(other, Time):
            return self.add_time(other)
        else:
            return self.increment(other)
            
    def __radd__(self, other):
        """Adds two Time objects or a Time object and a number."""
        return self.__add__(other)
            
    def addTime(self, other):
        seconds = self.timeToInt() + other.timeToInt()
        return int_to_time(seconds)
        
    def timeToInt(self):
        """Converts Time object to seconds integer.
        
        self: Time object.
        """
        assert self.validTime()
        minutes = self.hour * 60 + self.minute
        seconds = minutes * 60 + self.second  
        
        return seconds
    
    def increment(self, seconds):
        """increment: adds a given a number of seconds to Time object.
    
        self: Time object.
        seconds: int.
        """
        assert self.validTime()
        seconds += self.timeToInt()
        
        return int_to_time(seconds)
    
    def isAfter(self, other):
        """Checks if self follows other chronologically.
    
        self: Time object.
        other: Time object.
        """
        assert self.validTime() and other.validTime()
        s1 = self.timeToInt()
        s2 = other.timeToInt()
    
        return s1 > s2
        
    # An Invariant
    def validTime(self):
        """Validate Time object.
    
        Return 'True' if its a valid time or 'False' if otherwise.
    
        self: Time object.
        """
        if self.hour < 0 or self.minute < 0 or self.second < 0:
            return False
        if self.minute >= 60 or self.second >= 60:
            return False
        return True
    
    
if __name__ == "__main__":
    t = Time(3, 10)
    print(t)