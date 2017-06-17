import cwd
from time import *

def mul_time(time, n):
    """Multiply time by n.
    
    time: Time object.
    n: int
    """
    assert valid_time(time)
    secs = time_to_int(time)
    secs *= n
    
    return int_to_time(secs)


def average_pace(race_time, distance):
    """Calculates pace(time/mile).
    
    time: Time object.
    distance: int miles.
    """ 
    assert valid_time(race_time)
    return mul_time(race_time, 1/distance)
    


if __name__ == "__main__":
    time = Time()
    time.hour = 1
    time.minute = 34
    time.second = 5
    print_time(mul_time(time, 3))
    print_time(time)
    pace = average_pace(time, 13.1)
    print("Time per mile")
    print_time(pace)
