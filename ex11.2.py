from collections import Counter, defaultdict

def histogram ( s ):
    '''
    Counts the number of times(frequency) a letter occurs in a string.
    
    s: str
    '''
    d = {}
    for c in s:
        d[c] = d.get(c, 0)
        d[c] += 1
    return d


def histogram(t):
    return dict(Counter(t))


def invert_dict ( d ):
    '''
    Inverts the given dict(d). Where the keys
    are values and values are keys.
    
    d: dict
    '''
    invert = {}
    for k in d:
        key = d[k]
        invert.setdefault(key, []).append(k)
    return invert


def invert_dict(d):
    invert = defaultdict(list)
    for k in d:
        val = d[k]
        invert[val].append(k)   
    return dict(invert) 
    
print(invert_dict(histogram("sarcastic")))