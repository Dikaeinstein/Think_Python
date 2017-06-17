def compare ( x, y ):
    '''
    compare: Compares the given arguments and returns 
             appropriate result based on the chained-conditionals
              
    x: value to compare
    y: value to compare
    '''
    if x > y:
        return 1
    elif x < y:
        return -1
    elif x == y:
        return 0
