def first ( word ):
    '''
    first: Returns the first character in a string
    
    word: Sequence of characters
    '''
    return word[0]

def last ( word ):
    '''
    last: Returns the last character in a string
    
    word: Sequence of characters
    '''
    return word[-1]

def middle ( word ):
    '''
    middle: Returns the remaining character in a string
            after slicing of the first and last characters
    
    word: Sequence of characters
    '''
    return word[1: -1]



def is_palindrome ( word ):
    '''
    is_palindrome: Boolean function that returns 'True' if word
                   palindrome or 'False' if otherwise
                   
    word: sequence of characters
    '''
    if len(word) <= 1:
        return True
    if first(word) != last(word):
        return False
    return is_palindrome(middle(word))


def is_palindrome ( word ):
    return word == word[::-1]

print(is_palindrome("steps on no pets"))