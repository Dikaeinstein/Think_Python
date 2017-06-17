def has_duplicates(t):
    '''
    Returns True if list(t) has duplicate elements 
    or False if otherwise.
    
    t: list
    '''
    l = sorted(t)
    i = 0
    # using while loop
    while i < len(l)-1:
        if l[i] == l[i+1]:
            return True
        i += 1
    return False
    
    
def has_duplicates(t):
    '''
    Returns True if list(t) has duplicate elements 
    or False if otherwise.
    
    t: list
    '''
    l = sorted(t)
    previous = ""
    # using while loop
    for e in l:
        if previous == e:
            return True
        previous = e
    return False
       

def has_duplicates(d):
    '''
    Returns True if dict(d) has duplicate keys 
    or False if otherwise.
    
    d: dict
    '''
    previous = ""
    for k in d:
        if previous == k:
            return True
        previous = k
    return False
     
        
    
t = [1, 2, 3, 4, 2, 6, 3]    
print(has_duplicates(t))
print(t)