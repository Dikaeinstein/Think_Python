def fibonacci ( n ):
    '''
    fibonacci: Generates the fibonacci series
    
    n: 
    '''
    # Guard against incorrect input 
    if n < 0 or (not isinstance(n, int)):
        return "Error: n is either negative or not an integer" 
    if n == 0:
        return 0
    elif  n == 1:    
        return 1
    else: 
        return fibonacci(n-1) + fibonacci(n-2)


print(fibonacci(10.8))