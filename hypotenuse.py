import math
def hypotenuse ( opp, adj ):
    '''
    hypotenuse: Calculates the hypotenuse of a 
                right-angle triangle
    
    opp: Length of side opposite the hypotenuse
    adj: Length of side adjacent the hypotenuse   
    '''         
    dsquared = opp**2 + adj**2
    return math.sqrt(dsquared)


print(hypotenuse(3, 4))