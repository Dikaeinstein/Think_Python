def rotate_word ( word, rotate ):
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
    
    
print(rotate_word("ibm", -1))
        