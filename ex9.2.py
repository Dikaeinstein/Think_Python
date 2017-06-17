def has_no_e ( word ):
    for letter in word:
        if letter == "e":
            return False
    return True

# print(has_no_e("Thief"))
def main ():
    '''
    reads words.txt and loops through it and only prints 
    words that have no "e".
    '''
    words = open("/storage/sdcard1/python/think_python/test.txt", "r")
    
    for word in words:
        word = word.strip()
        if has_no_e(word):
            print(word)
            
            
main()
