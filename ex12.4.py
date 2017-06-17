def children ( word ):
    t = []
    if len(word) == 0:
        t.append("")
        return t
    
    elif len(word) > 2:
        mid = len(word) // 2
        t.append(word[1:])
        t.append(word[:-1])
        # for even length
        if len(word) % 2 == 0:
            t.append(word[:mid-1] + word[mid:])
        t.append(word[:mid] + word[mid+1:])
        return t
        
    elif len(word) == 2:
        t.append(word[1:])
        t.append(word[:-1])
        return t
        
    else:
        return t.append(word)
    


def is_reducible ( word ):
    if len(children(word)) == 0:
        return True
    for i in children(word):
        return is_reducible(i):

            
    

       
print(children("sprite"))