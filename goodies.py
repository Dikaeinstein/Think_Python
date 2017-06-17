"""
import math
# Conditional Expression
if x > 0:
    y = math.log(x)
else:
    y = float("nan")
    
# the above is equivalent to
y = math.log(x) if x > 0 else float("nan")
"""
def factorial(x):
    return 1 if x == 0 else x * factorial(x-1)
   
print(factorial(5))

# List Comprehension
# map
def capitalize_all(t):
    res = []
    for s in t:
        res.append(s.capitalize())
    return res
    
# the above is equivalent to:
def capitalize_all(t):
    return [s.capitalize() for s in t]
    
# filter
def only_upper(t):
    return [s for s in t if s.isupper()]
    
# Generator expression
g = (x**2 for x in range(5))
for val in g:
    print(val)
        