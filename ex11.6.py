def read_dictionary(filename='c06d'):
    """Reads from a file and builds a dictionary that maps from
    each word to a string that describes its primary pronunciation.

    Secondary pronunciations are added to the dictionary with
    a number, in parentheses, at the end of the key, so the
    key for the second pronunciation of "abdominal" is "abdominal(2)".

    filename: string
    returns: map from string to pronunciation
    """
    d = dict()
    fin = open(filename)
    for line in fin:

        # skip over the comments
        if line[0] == '#': continue

        t = line.split()
        word = t[0].lower()
        pron = ' '.join(t[1:])
        d[word] = pron

    return d


def is_homophone ( word1, word2, pronounce ):
    '''
    Checks if given words have same pronunciaton.
    
    pronounce: dictionary that maps from word to pronunciation.
    word1: string
    word2: string
    '''
    word1 = word1.lower()
    word2 = word2.lower()
    
    if word1 not in pronounce or word2 not in pronounce:
        return False
    
    return pronounce[word1] == pronounce[word2]
    
    
def check ( word, pron_dict, words_dict ):
    word1 = word[1:]
    word2 = word[0] + word[2:]
    
    if word1 not in words_dict or word2 not in words_dict:
        return False
    
    return is_homophone(word, word1, pron_dict) and is_homophone(word, word2, pron_dict)

    

def check_all ( pron_dict, words_dict ):
    for word in words_dict:
        if check(word, pron_dict, words_dict):
            print(word)

       
def words_dict ():
    fin = open("/storage/sdcard1/python/think_python/words.txt")
    words = {}
    for word in fin:
        word = word.strip().lower()
        words[word] = None
    fin.close()
    
    return words


filename = "/storage/sdcard1/python/think_python/c06d.txt"
d = read_dictionary(filename)
words = words_dict()
#print(is_homophone(d, "RACK", "WRACK"))
check_all(d, words)
        
        