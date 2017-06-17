def rotate_word ( word, rotate ):
    '''
    Rotates given word by 'rotate' and returns rotated word.
    
    word: str
    rotate: int
    '''
    rotated_word = ""
    if word.lower():
        start = ord("a")
    elif word.upper():
        start = ord("A")
    else:
        return word
    
    for letter in word:
        code = ord(letter) - start
        rotated_code = start + ((code +rotate) % 26)
        rotated_letter = chr(rotated_code)
        rotated_word += rotated_letter
    return rotated_word

   
def rotate_pairs ( d, word, n ):
    return rotate_word(word, n) in d
    
    
def all_rotate_pairs ( d, n, verbose=False ):
    '''
    Returns the number of rotate by 'n' pairs in given words dict(d). 
    Prints if verbose=True.
    
    d: dict
    n: int
    verbose: boolean
    '''
    count = 0
    for word in d:
        if rotate_pairs(d, word, n):
            count += 1
            if verbose:
                print(word, rotate_word(word, n))
    return count
    
    
    
def main ():
    def words_dict ():
        fin = open("/storage/sdcard1/python/think_python/words.txt", "r+")
        words = {}
        for word in fin:
            word = word.strip().lower()
            words[word] = None
        fin.close()
        return words
    
    words = words_dict()
    print(all_rotate_pairs(words, 13,True))


main()    