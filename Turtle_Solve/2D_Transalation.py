import turtle
import time

scale = 40
# Turtle setup
screen = turtle.Screen()
screen.setup(900, 700)
screen.tracer(0)
screen.title("2D Transformatoion")

# draw A Polygon function
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
axis.pensize(2)
axis.hideturtle()
axis.speed(0)

axis.penup()
axis.goto(-400,0)
axis.pendown()
axis.goto(400,0)

axis.penup()
axis.goto(0,-300)
axis.pendown()
axis.goto(0,300)

# Original triangle
triangle = [(-3,-2), (3,-2), (0,3)]
tx = 5
ty=3

# Original Triangle
original_pen = turtle.Turtle()
original_pen.color('red')
original_pen.pensize(5)
original_pen.hideturtle()
original_pen.speed(0)

draw_polygon(original_pen, triangle)

# Moving Traingle
moving_pen = turtle.Turtle()
moving_pen.color('green')
moving_pen.pensize(5)
moving_pen.hideturtle()
moving_pen.speed(0)

# Caluculate translation 
steps = 60
for i in range(steps+1):
    points = []
    t = i/steps
    for x , y in triangle :
        new_x = x + tx*t
        new_y = y + ty*t
        points.append((new_x, new_y))

    draw_polygon(moving_pen, points)
    screen.update()
    time.sleep(0.03)


screen.update()
screen.mainloop()