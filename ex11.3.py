cache = { "0,1": 2 }

def ack_memo ( m, n ):
    '''
    ack_memo: Evaluates Ackermann function with the given arguments.
              And optimize it by memoizing results to avoid repeating computation.
    
    m: Positive integer value
    n: Positive integer value
    '''
    # Guard against error from incorrect input
    if n < 0 or (not isinstance(n, int)):
        return "Error: n is either negative or not an integer"
    if m < 0 or (not isinstance(m, int)):
        return "Error: m is either negative or not an integer"
  
    key = str(m) + "," + str(n)
    if key in cache:
        return cache[key]
        
    # base case
    if m == 0:
        cache[key] = n + 1
        return cache[key]
        
    elif m > 0 and n == 0:
        cache[key] = ack_memo(m-1, 1)
        return cache[key]
    else:
        cache[key] = ack_memo(m-1, ack_memo(m, n-1))
        return cache[key]


print(ack_memo(3, 4))
print(cache)