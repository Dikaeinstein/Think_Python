def do_twice ( fn ):
    fn()
    fn()
 
def do_four ( fn ):
    do_twice(fn)
    do_twice(fn)
    
def print_twice ( s ):
    print(s * 2)

def print_four ( s ):
    print (s * 4)
 
def print_four_format ( s ):
    print (s * 4, end="") 

 
def right_justify ( s, n ):   
    length = len(s) 
    justify = n - length # no of justified space
    return (" " * justify) + s
    
    
def grid_linex ():
    print ("+", end=" ")
    print_four_format ("- ")
    print ("+", end=" ")
    print_four_format ("- ")
    print ("+")
    
def grid_liney ():
    print (right_justify("|", 0), end="")
    print_twice(right_justify("|", 10))

       
def draw_grid ():
    grid_linex()
    do_four(grid_liney)
    grid_linex()
    do_four(grid_liney)
    grid_linex()

    

def grid_line4x ():
    print("+", end=" ")
    print_four_format("- ")
    print("+", end=" ")
    print_four_format("- ")
    print("+", end=" ")
    print_four_format("- ")
    print("+", end=" ")
    print_four_format("- ")
    print("+", end=" ")
    
def grid_line4y ():
    print(right_justify("|", 0), end="")
    print_four(right_justify("|", 10))


def draw_four_grid ( ):
    grid_line4x()
    do_four(grid_line4y)
    grid_line4x()
    do_four(grid_line4y)
    grid_line4x()
    do_four(grid_line4y)
    grid_line4x()
    do_four(grid_line4y)
    grid_line4x()
    
    
  
# draw_grid()
draw_four_grid()
