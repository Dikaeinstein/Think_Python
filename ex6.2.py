def ack ( m, n ):
    '''
    ack: Evaluates Ackermann function with the given arguments
    
    m: Positive integer value
    n: Positive integer value
    '''
    # Guard against error from incorrect input
    if n < 0 or (not isinstance(n, int)):
        return "Error: n is either negative or not an integer"
    if m < 0 or (not isinstance(m, int)):
        return "Error: m is either negative or not an integer"
    
    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return ack(m-1, 1)
    else:
        return ack(m-1, ack(m, n-1))


print(ack(3, 4))