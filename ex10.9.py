import cwd

def words_list():
    '''
    Reads the file 'words.txt'. Traverse the text file, 
    strip whitespace, append each word to a list
    and return list of words.
    '''
    fin = open("words.txt", "r+")
    words = []
    for word in fin:
        word = word.strip()
        words.append(word)
    return words
    
    
def words_list():
    with open("words.txt") as fin:
        return [word.strip() for word in fin]


if __name__ == "__main__":
    for word in words_list():
        print(word)
    

    