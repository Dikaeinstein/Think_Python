def has_no_letter ( word, avoid ):
    for letter in word:
        if letter == avoid:
            return False
    return True


def avoids ( word, forbidden ):
    word = word.lower()
    forbidden = forbidden.lower()
    for for_letter in forbidden:
       if not has_no_letter(word, for_letter):
           return False
    return True


print(avoids("solomon", "aeiu"))