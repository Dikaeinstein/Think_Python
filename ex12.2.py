def all_anagrams ( filename ):
    '''
    Reads a word list file and stores all sets of anagrams in dictionary.
    
    filename: str
    '''
    fin = open(filename)
    d = {}
    for word in fin:
        word = word.strip().lower()
        k = "".join(sorted(word))
        d.setdefault(k, []).append(word)
                
    return d     
    

def print_all_anagrams ( d ):
    '''
    Iterates given dict(d) and print all sets of anagram.
    
    d: dict
    '''
    for i in d.values():
        if len(i) > 1:
            print(i)
        

def print_all_anagrams_inorder ( d ):
    '''
    Iterates given dict(d) and print all sets of anagram in order.
    
    d: dict
    '''
    t = []
    for i in d.values():
        if len(i) > 1:
            t.append((len(i), i))
    t.sort()
    
    for i in t:
        print(i)
       


def bingo ( d, n ):
    '''
    Filter given dict(d) for keys of length(n)=8.
    
    d: dict
    n: int 
    '''
    res = {}
    for word, anagram in d.items():
        if len(word) == n:
            res[word] = anagram
            
    return res


filename = "/storage/sdcard1/python/think_python/words.txt"
d = all_anagrams(filename)
#print_all_anagrams(d) 
bingos = bingo(d, 8) 
print_all_anagrams_inorder(bingos)  

              
                
            
        
        