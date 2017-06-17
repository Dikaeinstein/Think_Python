'''def factorial ( n ):
    if n < 0 or (not isinstance(n, int)):
        return "Error: n is either negative or not an integer"
    if n == 0:
        return 1
    else:
        recurse = factorial(n-1)
        result = n * recurse
        return result


def factorial ( n ):
    # n = int(abs(n))
    if n < 0 or (not isinstance(n, int)):
        return "Error: n is either negative or not an integer"
    if n < 2:
        return 1
    return n * factorial(n-1)
'''
  

def factorial ( n, a=1 ):
    #n = int(abs(n))
    #a = int(abs(a))    
    if n < 2:
        return a
    return factorial(n-1, a*n)


def trampolining ( res ):       
    while str(type(res))[7:-1] == "function":
        res = res()
    return res


# optimized to scale even for large values of n
# to avoid exceeding maximum recursion stack depth
# using loop ( recursion unrolling )
'''
def factorial ( n ):
    if n < 0 or (not isinstance(n, int)):
        return "Error: n is either negative or not an integer"
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result
'''
   
print(trampolining(factorial(1000)))