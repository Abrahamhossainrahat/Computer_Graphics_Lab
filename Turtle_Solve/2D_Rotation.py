import turtle
import time 
import math

# Turtle setup 
screen = turtle.Screen()
screen.setup(900,700)
screen.title("2D Rotation")
screen.tracer(0)

scale = 40

# Draw a Polygon 
def draw_polygon(pen, points) :
    pen.clear()

    pen.penup()
    x, y = points[0]
    pen.goto(x*scale, y*scale)

    pen.pendown()
    for x, y in points[1:] :
        pen.goto(x*scale, y*scale)
    
    x, y = points[0]
    pen.goto(x*scale, y*scale)
    pen.penup()

# X & Y axis generate 
axis = turtle.Turtle()
axis.color('gray')
axis.hideturtle()
axis.pensize(3)

axis.penup()
axis.goto(-400,0)
axis.pendown()
axis.goto(400, 0)

axis.penup()
axis.goto(0,-300)
axis.pendown()
axis.goto(0, 300)

# Original triangle
triangle = [
    (1, 1),
    (4, 1),
    (2.5, 4)
]
angle = 90

#  Original Triangle draw
original_pen = turtle.Turtle()
original_pen.color('red')
original_pen.hideturtle()
original_pen.speed(0)
original_pen.pensize(5)

draw_polygon(original_pen, triangle)

# Rotate the triangle
moving_pen = turtle.Turtle()
moving_pen.color('green')
moving_pen.hideturtle()
moving_pen.speed(0)
moving_pen.pensize(5)

steps = 60
for i in range(steps + 1) :
    points = []
    current_angle = angle * i/steps
    rad = math.radians(current_angle)
    for x, y in triangle :
        new_x = x*math.cos(rad) - y*math.sin(rad)
        new_y = x*math.sin(rad) + y*math.cos(rad)
        points.append((new_x, new_y))

    draw_polygon(moving_pen, points)
    screen.update()
    time.sleep(0.03)

screen.mainloop()