def is_sorted ( t ):
    '''
    Returns True if list(t) is sorted or False if otherwise.
    
    t: list
    '''
    return t == sorted(t)
        
        
print(is_sorted([1, 2, 2]))
print(is_sorted(["b", "a"]))
        