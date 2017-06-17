def histogram ( s ):
    d = {}
    for c in s:
        d[c] = d.get(c, 0) + 1
        
    return d


def most_frequent ( s ):
    '''
    Prints all the letters in decreasing order of frequency.
    
    s: str
    '''
    d = histogram(s)
    l = d.items()
    t = []
    for letter, freq in l:
        t.append((freq, letter))
    
    t.sort(reverse=True)
    
    for e in t:
        print(e)
        
    
    
    
most_frequent("sarcastic")
    