def has_no_letter(word, avoid):
    for letter in word:
        if letter == avoid:
            return False
    return True
    
    
def avoids(word, avoid):
    return not set(word).issubset(avoid)


def uses_only ( word, available ):
    word = word.lower()
    available = available.lower()
    for letter in word:
        if letter == " ":
            pass
        elif has_no_letter(available, letter):
            return False
    return True


def uses_only ( word, available ):
    word = word.lower()
    availablr = available.lower()
    for letter in word:
        if letter == " ":
            pass
        elif letter not in available:
            return False
    return True
    

print(uses_only("Hoe alfalfa", "acefhlo"))
print(avoids("solomon", "soloman"))