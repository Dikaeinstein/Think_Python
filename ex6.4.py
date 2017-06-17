def is_divisible ( a, b ):
    '''
    is_divisible: Boolean function that returns 'True' if
                  a is divisible by b or false if otherwise
    '''
    return a % b == 0
    

def is_power ( a, b ):
    '''
    is_power: a is a power of b if a is divisible by b and
              and a/b is power of b
    '''
    is_power.called += 1  
    if is_power.called > 2:
        return True
    return is_divisible(a,b) and is_power(a/b,b)

is_power.called = 0


print(is_power(2,2))