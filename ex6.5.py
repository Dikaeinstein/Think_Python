def gcd ( a, b ):
    '''
    gcd: Calculates the Greatest Common Divisor of the
         given numbers
    
    a: Positive integer value
    b: Positive integer value
    '''
    # Guard against error from incorrect input
    if a < 0 or (not isinstance(a, int)):
        return "Error: a is either negative or not an integer"
    if b < 0 or (not isinstance(b, int)):
        return "Error: b is either negative or not an integer" 
    return a if b == 0 else gcd(b, a%b)


print(gcd(4,4))