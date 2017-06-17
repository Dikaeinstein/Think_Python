def is_between ( x, y, z ):
    if x <= y <= z:
        return True
    else:
        return False


print(is_between(4,5,6))