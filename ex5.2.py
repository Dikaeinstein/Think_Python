def check_fermat ( a, b, c, n):
    '''
    check_fermat: Checks to see if Fermat last theorem: a^n + b^n = c^n for n < 2
                  holds for the given numbers
                  
    a: integer number
    b: integer number
    c: integer number
    n: exponent integer number
    '''
    if n > 2:
        if (a**n) + (b**n) == c**n:
            print("holy smokes, Fermat was wrong")
        else:
            print("No, that doesn't work")
    else:
        print(True)



def input_check_format():
    '''
    input_check_format: reads input from user to fetch arguments
                        used to call check_fermat()
    '''                   
    print("Enter numbers:")
    a = input("Enter a: ")
    a = int(a)
    b = input("Enter b: ")
    b = int(b)
    c = input("Enter c: ")
    c = int(c)
    n = input("Enter n: ")
    n = int(n)
    check_fermat(a,b,c,n)    
    


input_check_format()           