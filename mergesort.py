def merge(left, right):
    """Merge two sorted lists.
    
    left: list 
    right: list
    """
    left = left[::-1]
    right = right[::-1]
    res = []
    
    while len(left) != 0 and len(right) != 0:
        if left[-1] < right[-1]:
            res.append(left.pop())
        else:
            res.append(right.pop())
    
    # extend the result list with the remaining elements of non-empty list
    res.extend(left) if len(left) > 0 else res.extend(right)
    return res
    
    
def merge_sort(l):
    '''Bisect list and sort recursively.
    
    l: list
    '''
    # base case
    if len(l) < 2:
        return l[:]
        
    # bisect list
    middle = int(len(l) // 2)
    left = l[:middle]
    right = l[middle:]
    return merge(merge_sort(left), merge_sort(right))
    
print(merge_sort([4,1,3,2]))          