def is_anagram ( word1, word2 ):
    '''
    Returns True if word1 is 'anagram' of word2 or False if otherwise.
    
    word1: str
    word2: str
    '''
    return sorted(word1) == sorted(word2)
    
    
    
print(is_anagram("silence", "listen"))
    