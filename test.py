from turtle import *

turtle = Turtle()
'''
colores = ["red", "purple", "orange", "blue", "green", "yellow"]
for i in range (6):
    p.color(colores[i])
    p.width(10)
    p.fd(70)
    p.rt(60)
'''
def circle(bounds):
    turtle.penup()
    center_x = bounds['x'] + bounds['width'] // 2
    bottom_y = bounds['y']
    turtle.setposition(center_x, bottom_y)
    turtle.pendown()

    turtle.circle(min(bounds['width'], bounds['height']) // 2)

def triangle(bounds):
    circle(bounds)

def square(bounds):
    circle(bounds)

def pentagon(bounds):
    circle(bounds)

def hexagon(bounds):
    circle(bounds)

def heptagon(bounds):
    circle(bounds)


done()

