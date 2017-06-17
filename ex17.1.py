class Time:
    """Represents the time of day.
    
    attributes: hiur, minute, second.
    """
    def __init__(self, hour=0, minute=0, second=0):
        minutes = hour * 60 + minute
        self.second = minutes * 60 + second
        
    def __str__(self):
        minutes, second = divmod(self.second, 60)
        hour, minute = divmod(minutes, 60)
        return "{0:02.0f}:{1:02.0f}:{2:02.0f}".format(hour, minute, second)
       
    def __add__(self, other):
        """Adds two Time objects or Time and number of seconds.
        
        other: Time object or number of seconds
        """
        if isinstance(other, Time):
            return self.add_time(other)
        else:
            return self.increment(other)
        
    def __radd__(self, other):
        """Adds two Time objects or a Time object and a number."""
        return self.__add__(other)
        
    def print_time(self):
        print(self)    
    
    def add_time(self, other):
        """Adds two Time objects."""
        seconds = self.second + other.second
        return int_to_time(seconds)
        
    def time_to_int(self):
        """Converts Time object to number of seconds.
        
        self: Time object.
        """
        assert self.valid_time()      
        return self.second
        
    def increment(self, seconds):
        """increment: adds a given a number of seconds to Time object.
    
        self: Time object.
        seconds: int.
        """
        assert self.valid_time()
        seconds += self.second 
        return seconds
        
    def is_after(self, other):
        """Checks if self follows other chronologically.
    
        self: Time object.
        other: Time object.
        """
        assert self.valid_time() and other.valid_time()    
        return self.second > other.second
        
    def int_to_time(secs):
        """Converts seconds integer to Time object.
    
        secs: int.
        """   
        return Time(0, 0, secs)
        
    # An Invariant
    def valid_time(self):
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
    t = Time(23, 30, 59)
    print(t)