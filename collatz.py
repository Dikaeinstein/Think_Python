def collatz ( n ):
    '''
    collatz: According to Collatz Conjecture generates a sequence that terminates at 1.
    
    n: positive integer that starts the sequence
    '''
    # recursion unrolling
    while n != 1:
        print(n)    
        if n % 2 ==0:      # n is even
            n //= 2
        else:              # n is odd 
            n = n * 3 + 1
    print(n)
            

# recursive collatz conjecture
def collatz ( n ):
    print(n)
    if n == 1:        # base case
        return
    if n % 2 == 0:     # n is even
        n = n // 2
    else:              # n is odd
        n = n * 3 + 1
    
    return collatz(n)
    
    
          
collatz(4)
        