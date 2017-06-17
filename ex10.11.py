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
        return 
    return t[index] == x


def is_reverse_pair ( t, word ):
    '''
    Returns True if list(t) contains reverse of word.
    Or False if it doesn't.
    
    t: list
    word: str
    '''
    return in_bisect(t, word[::-1])
        
#print(is_reverse_pair("dika", "akid"))

    
    
def all_reverse_pair ():
    count = 0
    words = words_list()
    for word in words:
        if is_reverse_pair(words, word):
            count += 1
            print(word, word[::-1])
    return count

   
def main ():
    print(all_reverse_pair())

   
main()
        
        
        
    
    