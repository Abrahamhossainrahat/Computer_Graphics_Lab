## Translation And Totation 
import turtle 
import time
import math

scale = 40

# Screen Steup 
screen = turtle.Screen()
screen.setup(900,700)
screen.title("2D Transformation")
screen.tracer(0)

# Draw X and Y axis 
axis = turtle.Turtle()
axis.hideturtle()
axis.speed(0)
axis.color('gray')
axis.pensize(2)

axis.penup()
axis.goto(-400, 0)
axis.pendown()
axis.goto(400,0)

axis.penup()
axis.goto(0, -300)
axis.pendown()
axis.goto(0, 300)

# Draw Polygon Function
def draw_polygon(pen, points) :
    pen.clear()

    pen.penup()
    x, y = points[0]
    pen.goto(x*scale,y*scale)

    pen.pendown()
    for x , y in points[1:] :
        pen.goto(x*scale, y*scale)

    x, y = points[0]
    pen.goto(x*scale,y*scale)
    pen.penup()

    return points

        
# Original Triangle 
triangle = [(-3,-2), (0,3), (3,-2)]
tx = 5
ty = 3

# Original Object 
original_pen = turtle.Turtle()
original_pen.hideturtle()
original_pen.color('red')
original_pen.speed(0)
original_pen.pensize(5)
draw_polygon(original_pen, triangle)

# Moving Object 
moving_pen = turtle.Turtle()
moving_pen.hideturtle()
moving_pen.pensize(5)
moving_pen.color('green')
moving_pen.speed(0)

# Transaltion Annimation 

steps = 60
for i in range(steps+1) :
    t = i/steps
    points = []
    for x, y in triangle :
        new_x = x + tx*t
        new_y = y + ty*t
        points.append((new_x, new_y))
    
    translation_traingle = draw_polygon(moving_pen, points)
    screen.update()
    time.sleep(0.01)

# Rotate the triangle
rotate_pen = turtle.Turtle()
rotate_pen.color('blue')
rotate_pen.hideturtle()
rotate_pen.speed(0)
rotate_pen.pensize(5)

steps = 60
angle = 90
for i in range(steps + 1) :
    points = []
    current_angle = angle * i/steps
    rad = math.radians(current_angle)
    for x, y in  translation_traingle :
        new_x = x*math.cos(rad) - y*math.sin(rad)
        new_y = x*math.sin(rad) + y*math.cos(rad)
        points.append((new_x, new_y))

    draw_polygon(rotate_pen, points)
    screen.update()
    time.sleep(0.03)

#screen.update()

screen.mainloop()
