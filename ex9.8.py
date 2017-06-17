def has_palindrome ( i, start, length ):
    """Checks if the string representation of i has a palindrome.

    i: integer
    start: where in the string to start
    length: length of the palindrome to check for
    """
    s = str(i)[start: length]
    return s == s[::-1]

#print(has_palindrome("soos", 0, 4))

def check ( number ):
    """Checks if the integer (number) has the desired properties.

    number: int
    """
    return (has_palindrome(number, 2, 6) and 
            has_palindrome(number+1, 1, 6) and 
            has_palindrome(number+2, 1, 5) and
            has_palindrome(number+3, 0, 6)) 



def check_all ():
    """Enumerate the six-digit numbers and print any number that has the desired properties.
    """
    i = 100000
    while i < 999999:
        if check(i):
            print(i)
        i += 1

    
print('The following are the possible odometer readings:')
check_all()