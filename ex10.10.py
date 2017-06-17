def in_bisect ( t, x ):
    '''
    Performs binary searchs for x in list(t). 
    Bisecting(splitting) list recursively until x is found
    and returns True or False if otherwise.
    
    t: list
    x: element
    '''
    # base case 1
    if len(t) == 0:
        return False
        
    middle = int(len(t) // 2)   
    # base case 2
    if t[middle] == x:
        return True
        
    if t[middle] > x:
        return in_bisect(t[:middle], x)
    else:
        return in_bisect(t[middle+1:], x)


# in_bisect cheat using in-built bisect.bisect_left()
# function from bisect module
def in_bisect ( t, x ):
    import bisect
    index = bisect.bisect_left(t, x)
    if index >= len(t):
        return 
    return index
    
    
def words_list ():
    fin = open("/storage/sdcard1/download/words.txt", "r+")
    words = []
    for word in fin:
        word = word.strip()
        words.append(word)
    fin.close()
    return words
    
    
#print(in_bisect([1,2,3,4,4],3))
def main ():
    words = words_list()
    print(in_bisect(words, "polymath"))
    
    
main()
    
            