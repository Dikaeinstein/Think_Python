def is_triangle ( l1, l2, l3 ):
    if l1 > (l2 + l3):
        print("No")
    elif l2 > (l1 + l3):
        print("No")
    elif l3 > (l1 + l2):
        print("No")
    else:
        print("Yes")

is_triangle(70, 30, 30)