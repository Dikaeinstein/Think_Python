def recurse ( n, s ):
    '''
    recurse: is a function that keeps calling itself
             until the base case: n == 0 is reached
    '''
    if ( n == 0 ):
        print(s)
    else:
        recurse(n-1, n+s)

recurse(-1, 0)