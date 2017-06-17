import random
randint = random.randint

def has_duplicates(t):
    '''
    Returns True if list(t) has duplicate elements 
    or False if otherwise.
    
    t: list
    '''
    l = sorted(t)
    i = 0
    while i < len(l)-1:
        if l[i] == l[i+1]:
            return True
        i += 1
    return False


def has_duplicates(t):
    return len(set(t)) == len(t)  
    
def bday_sample ( n ):
    '''
    Randomly generate birthday sample of n-persons.
    
    n: int
    '''
    sample = []
    for i in range(n):
        bday = randint(1, 365)
        sample.append(bday)
    return sample
        
        
def count_matches ( num_simulations, num_students ):
    '''
    Counts the number of samples that contain atleast one(1) birthday match. 
    After a given number of simulations.
    
    num_simulations: int
    num_students: int
    '''
    count = 0
    for i in range(num_simulations):
        sample = bday_sample(num_students)
        if has_duplicates(sample):
            count += 1
    return count
    
        
def main ():
    num_simulations = 1000
    num_students = 23
    count = count_matches(num_simulations, num_students)
    print("After %d simulation" % num_simulations)
    print("with %d students" % num_students)
    print('there were %d simulations with at least one match' % count)
    
main()
     