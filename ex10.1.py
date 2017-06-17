def nested_sum ( list_of_lists ):
    '''
    Reduce the list of lists to single result by
    summing the elements/items in the nested lists.
    
    list_of_lists: list
    '''
    acc = 0
    for nested in list_of_lists:
        for item in nested:
            acc += item
    return acc
            
# using builtin list method: 'sum'
def nested_sum ( list_of_lists ):
    '''
    Reduce the list of lists to single result by
    summing the elements/items in the nested lists.
    
    list_of_lists: list
    '''
    acc = 0
    for nested in list_of_lists:
        acc += sum(nested)
    return acc

    
t = [[1, 2], [3], [4, 5, 6]] 
print(nested_sum(t))      