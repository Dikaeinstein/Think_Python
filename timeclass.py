from copy import deepcopy

class Time:
    """Represents the time of day.
    
    attributes: hour, minute, second.
    """
    pass
    
    
def print_time(time):
    """Prints Time object in the form h:m:s.
    
    time: Time object.
    """
    print("{0:02.0f}:{1:02.0f}:{2:02.0f}".format(time.hour, time.minute, time.second))


def time_to_int(time):
    """Converts Time object to seconds integer.
    
    time: Time object.
    """
    minutes = time.hour * 60 + time.minute
    seconds = minutes * 60 + time.second  
    return seconds          


def int_to_time(secs):
    """Converts seconds integer to Time object.
    
    secs: int.
    """
    time = Time()
    minutes, time.second = divmod(secs, 60)  
    time.hour, time.minute = divmod(minutes, 60)
    
    return time
    
    
def is_after(t1, t2):
    """Checks if t1 follows t2 chronologically.
    
    t1: Time object.
    t2: Time object.
    """
    s1 = time_to_int(t1)
    s2 = time_to_int(t2)
    
    return s1 > s2
    

def normalize_time(time):
    """Normalize time by carrying over excess seconds and minutes recursively.
    
    time: Time object.
    """
    if time.second < 60 and time.minute < 60:
        return time
    # carry over excess seconds  
    if time.second >= 60:
        time.second -= 60
        time.minute += 1
    # carry over excess minutes    
    if time.minute >= 60:
        time.minute -= 60
        time.hour += 1
        
    return normalize_time(time)

   
def increment(time, seconds):
    """increment: adds a given a number of seconds to Time object.
    
    time: Time object.
    seconds: int.
    """
    assert valid_time(time)
    secs = time_to_int(time)
    secs += seconds
    
    return int_to_time(secs)
     

# An Invariant
def valid_time(time):
    """Validate Time object.
    
    Return 'True' if its a valid time or 'False' if otherwise.
    
    time: Time object.
    """
    if time.hour < 0 or time.minute < 0 or time.second < 0:
        return False
    if time.minute >= 60 or time.second >= 60:
        return False
    return True

                 
if __name__ == "__main__":
    # first Time object
    t = Time()
    t.hour = 5
    t.minute = 21
    t.second = 34
    # second Time object
    t2 = Time()
    t2.hour = 11
    t2.minute = 59
    t2.second = 30
    print_time(t)
    print_time(t2)
    print(is_after(t2, t))
    print_time(increment(t2, 160))
    