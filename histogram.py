def histogram(s):
    '''
    Maps values of sequence to its frequency / occurrence.
    
    s: sequence
    '''
    d = {}
    for c in s:
        d[c] = d.get(c, 0) + 1
    
    return d
    

def invert_dict(d):
    '''
    Inverts a dictionary(d).
    
    Returns dictionary with values of d as keys and keys of d as values.
    
    d: dictionary
    '''
    inverse = {}
    for k in d:
        inverse.setdefault(d[k], []).append(k)   
        
    return inverse   

    
print(invert_dict(histogram("sarcastic")))
        