import cwd
from turtle import Turtle
import polygon
import Circle
    
def draw_circleircirclele(t, circle):
    '''Draws circle using turtle object.
    
    t: Turtle object.
    circle: Circle object.
    '''
    t.pu()
    t.goto(circle.center.x, circle.center.y)
    t.fd(circle.radius)
    t.pd()
    polygon.circle(t, circle.radius)
    
    
if __name__ == "__main__":
    t = Turtle()
   
    # draw the axes
    length = 400
    t.fd(length)
    t.bk(length)
    t.lt(90)
    t.fd(length)
    t.bk(length)
    
    # draw circle
    center = Point()
    center.x = 150.0
    center.y = 100.0
    circle = Circle()
    circle.center = center
    circle.radius = 75.0
    draw_circle(t, circle)