#-*-coding:utf8;-*-
import bisect
def words_list ():
    fin = open("/storage/sdcard1/download/words.txt", "r+")
    words = []
    for word in fin:
        word = word.strip()
        words.append(word)
    fin.close()
    return words
    
    
def in_bisect ( t, x ):
    index = bisect.bisect_left(t, x)
    if index >= len(t):
        return False
    return t[index] == x
    
    
def interlock ( words_list, word, flag=False ):   
    '''
    Interlock: two words are said to interlock 
               if alternate letter from them
               forms a new word.
    Returns 'True' if words_list contains an interlocked pair. 
    Formed from the given word. 
    
    words_list: list
    word: str
    flag: boolean
    '''
    #word1 = 
    #word2 = 
    #i = 0
    #while i < len(word)-1:
        #word1 += word[i]
        #word2 += word[i+1]
        #i += 2
    # concise / terse form of generating
    # two words by using slice operator
    # and stepping by 2
    word1 = word[::2]
    word2 = word[1::2]
    if in_bisect(words_list, word1) and in_bisect(words_list, word2):
        if flag:
            print(word1, word2)
        return True
    return False
    

def interlock_gen ( words_list, word, n=2, flag=False ):
    n_way = ""
    for i in range(n):
        inter = word[i::n]
        if not in_bisect(words_list, inter):
            return False
        n_way += (inter+" ")
    if flag:
        print(n_way)
    return True
    


def main ():
    words = words_list()
    #print(interlock(words, "schooled"))
    for word in words:
        # for three_way interlocked words n=3
        interlock_gen(words, word, 3, True)
        
        
main()
    
        
    