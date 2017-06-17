import cwd
from copy import deepcopy
from math import sqrt

class Point:
    '''Represents a point in 2-D space.'''
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y

    def __str__(self):
        return "({0}, {1})".format(self.x, self.y)
    
    # Type-Based dispatch    
    def __add__(self, other):
        if isinstance(other, Point):
            return self.add_point(other)
        else:
            return self.add_tuple(other)
        
    def add_point(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Point(x, y)
        
    def add_tuple(self, t):
        assert len(t) == 2
        x = self.x + t[0]
        y = self.y + t[1] 
        return Point(x, y)
           
    def dist_between_points(self, other):
        '''Calculate the distance between two points in 2-D space.
    
        self: point object.
        other: point object.
        '''
        distance = sqrt((other.y- self.y)**2+(other.x-self.x)**2)
    
        return distance


class Rectangle:
    '''Represents a rectangle.'''
    def __init__(self, width, height, corner):
        self.width = width
        self.height = height
        self.corner = corner    

    def move_rectangle(self, dx, dy):
        '''Move rectangle to new point.
        
        rect: Rectangle object.
        dx: displacement in x-direction.
        dy: displacement in y-direction.
        '''   
        self.corner.x += dx
        self.corner.y += dy
    
    def move_rect(self, dx, dy):
        '''Create rectangle, Move it to new point and return the new rectangle.
        
        self: Rectangle object.
        dx: displacement in x-direction.
        dy: displacement in y-direction.
        '''  
        new_rect = deepcopy(self)
        move_rectangle(new_rect, dx, dy)
        
        return new_rect

   
if __name__ == "__main__":
    p1 = Point(-3.0, -4.0)
    p2 = Point(3.0, 4.0)    
    rect = Rectangle(100.0, 60.0, p1)
    print(p1)
    print(p2)
    print(p1+p2)
    print(p2+(6.0, 9.0))
    print(p1.dist_between_points(p2))
    rect.move_rectangle(5.0, 7.0)
    print(rect.corner.x)
    print(rect.corner.y)
    #rect.move_rect(5.0, 7.0)
    