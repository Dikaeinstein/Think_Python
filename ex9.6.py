def is_abecedarian ( word ):
    if len(word) <= 1:
        return True    
    previous = word[0]
    for letter in word:
        if previous > letter:
            return False
        previous = letter
    return True


def is_abecedarian ( word ):
    if len(word) <= 1:
        return True
    if word[0] > word[1]:
        return False
    return is_abecedarian(word[1:])

print(is_abecedarian(""))