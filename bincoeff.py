cache = {}

def binomial_coeff(n, k):
    """Compute the binomial coefficient 'n choose k'.
    
    n: number of trials
    k: number of successes
    
    returns: int
    """
    
    if k == 0:
        return 1
    if n == 0:
        return 0
    try:
        return cache[n,k]
    except KeyError:
        cache[n,k] = binomial_coeff(n-1, k-1) + binomial_coeff(n-1, k)
        return cache[n,k]
    
    
def binomial_coeff(n, k=0):
    if k == 0:
        return 1
    return 0 if n == 0 else binomial_coeff(n-1, k-1) + binomial_coeff(n-1, k)
    
    
if __name__ == "__main__":
    print(binomial_coeff(4, 2))