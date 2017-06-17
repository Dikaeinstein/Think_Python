def uses_only(word, available):
    word = word.lower()
    available = available.lower()
    for letter in word:
        if letter not in available:
            return False
    return True
    


def uses_all(word, required):
    # early check: word cannot use all of contains
    # if its length is not equal to length of contains
    if len(word) != len(required):
        return False
    '''   
    for letter in word:
        if letter not in required:
            return False
    return True
    '''
    return uses_only(word, required)
    

def uses_all(word, required):
    return all(letter in word for letter in required)

print(uses_all("solomon", "soloman"))

