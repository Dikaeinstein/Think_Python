#!/data/data/org.qpython.qpy3/files/bin/python

def right_justify(s): 
    '''Right justify string.
    
    Justifies the string with leading space that the last
    letter of the string is in column 70 of display.
    
    s: string
    
    Returns right-justified string 
    '''
    length = len(s) 
    # no of leading space
    justify = 70 - length 
    return (" " * justify) + s
    
if __name__ == "__main__":
    print (right_justify("monty"))


#import os
#print(os.getcwd()) 
#print(os.path.abspath("py.txt")) 
#os.chdir(os.path.dirname(os.path.abspath('__file__')))

    