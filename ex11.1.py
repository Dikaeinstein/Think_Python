import cwd()

def words_list ():
    fin = open("words.txt" , "r+")
    words = []
    for word in fin:
        word = word.strip()
        words.append(word)
    fin.close()
    
    return words
    
    
def in_bisect ( t, x ):
    import bisect
    index = bisect.bisect_left(t, x)
    if index >= len(t):
        return 
    
    return index
    
    
def words_dict ():
    fin = open("words.txt", "r+")
    words = {}
    for word in fin:
        word = word.strip().lower()
        words[word] = None
    fin.close()
    
    return words
    

def words_set():
    with open("words.txt") as fin:
        s = set()
        for word in fin:
            s.add(word.strip())
        return s
    

print("polymath" in words_list())    
print("polymath" in words_dict())
print(in_bisect(words_list(), "polymath"))
    

       