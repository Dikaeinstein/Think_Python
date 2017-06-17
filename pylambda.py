def increment( n ): 
    return lambda m : n+m
f = increment(43)
print(f(1))
print(f(2))
print(f(3))