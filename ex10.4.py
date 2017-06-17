def chop ( t ):
    '''
    Modifies list(t) by choping off its first and last elements.
    
    t: list
    '''
    del t[0]
    del t[-1]
    return None
    

t = [1, 2, 3, 4]    
print(chop(t))
print(t)