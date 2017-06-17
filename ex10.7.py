def has_duplicates ( t ):
    '''
    Returns True if list(t) has duplicate elements 
    or False if otherwise.
    
    t: list
    '''
    l = sorted(t)
    i = 0
    while i < len(l)-1:
        if l[i] == l[i+1]:
            return True
        i += 1
    
    return False


def has_duplicates ( t ):
    '''
    Returns True if list(t) has duplicate elements 
    or False if otherwise.
    
    t: list
    '''
    # terse and optimised version using set
    return len(set(t)) == len(t)

    
t = [1, 2, 3, 4, 2, 6, 3]    
print(has_duplicates(t))
print(t)
        