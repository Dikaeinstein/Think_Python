def cumsum ( t ):
    '''
    Maps list(t) to cummulative sum of its elements. 
    
    t: list
    '''
    cum_list = []
    total = 0
    for item in t:
        total += item
        cum_list.append(total)
        
    return cum_list
    
    
    
    
print(cumsum([2, 1, 3]))
        