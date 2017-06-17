def histogram(s):
    '''Maps letter of string to its frequency / occurrence.
    
    s: string
    '''
    d = {}
    for c in s:
        d[c] = d.get(c, 0) + 1
    
    return d


def is_isogram(word, n=1):
    '''Every letter in 'word' must appear equal times.
    
    word: string
    n: the max no of occurence each of letter.
    '''
    if n == 1:
        return len(set(word)) == len(word)
        
    word_hist = histogram(word)   
    freqs = list(word_hist.values())
    previous = freqs[0]
    
    for freq in freqs:
        if previous > freq:
            return False  
            
    return True  
    

if __name__ == "__main__":
    print(is_isogram.__doc__)
    print(is_isogram("sarrcasttiic"))