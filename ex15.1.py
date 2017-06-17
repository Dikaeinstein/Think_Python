import cwd
from copy import deepcopy
from distance_between_points import dist_between_points, Point, Rectangle

class Circle:
    '''Represents a circle.
    
    attributes: center, radius.
    '''
    pass
    

def point_in_circle(point, circle):
    '''Checks whether a point lies inside a circle(or on its boundary).
    
    Calculates the distance between the center of the circle and given point. 
    And compares it with the radius of the circle.
    
    circle: Circle object.
    point: Point object
    '''
    d = dist_between_points(point, circle.center)
    
    return d <= circle.radius
    

def rect_in_circle(rect, circle):
    '''Checks whether a rect lies inside a circle(or on its boundary).
    
    rect: Rectangle object.
    circle: Circle object.
    '''
    p = deepcopy(rect.corner)
    if not point_in_circle(p, circle):
        return False
        
    p.x += rect.width
    if not point_in_circle(p, circle):
        return False

    p.y -= rect.height  
    if not point_in_circle(p, circle):
        return False
        
    p.x -= rect.width
    if not point_in_circle(p, circle):
        return False    
               
    return True      
    
    
def rect_circle_overlap(rect, circle):
    p = deepcopy(rect.corner)
    p.x += rect.width
    if point_in_circle(p, circle):
        return True

    p.y -= rect.height  
    if point_in_circle(p, circle):
        return True
        
    p.x -= rect.width
    if point_in_circle(p, circle):
        return True   
               
    return False    


if __name__ == "__main__":    
    circle = Circle()
    circle.center = Point()
    circle.center.x = 150
    circle.center.y = 100
    circle.radius = 75
    point = Point()
    point.x = 100.0
    point.y = 150.0
    print(point_in_circle(point, circle))
    rect = Rectangle()
    rect.corner = point
    rect.width = 30.0
    rect.height = 20.0
    print(rect_in_circle(rect, circle))
    print(rect_circle_overlap(rect, circle))




    