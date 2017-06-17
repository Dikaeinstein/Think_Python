def is_double_3consec ( word ):
    '''
    is_double_3consec: traverses given word and returns 'True' if it contains 
    three consecutive double letters. Otherwise return 'False'.
    '''
    count = 0
    i = 0
    while i < len(word)-1:
        if word[i] == word[i+1]:
            count += 1
            if count == 3:
                return True
            i += 1
        else:
            count = 0
        i += 1
    return False
    
    
print(is_double_3consec("mississippi"))
        