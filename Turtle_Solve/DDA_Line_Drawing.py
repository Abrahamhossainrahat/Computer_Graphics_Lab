import turtle 
import time 

scale = 30

def ddaLineDrawing(x1, y1, x2, y2) :
    points = []
    dx = x2 - x1
    dy = y2 - y1

    steps = int(max(abs(dx), abs(dy)))

    if steps == 0 :
        return [(round(x1), round(y1))]

    x_increment = dx / steps
    y_increment = dy / steps

    for i in range(steps+1) :
        points.append((round(x1), round(y1)))
        x1 += x_increment
        y1 += y_increment

    return points 


# Turtle Setup 
screen = turtle.Screen()
screen.setup(900, 700)
screen.title("DDA Line Drawing Algorithm")
screen.tracer(0)


# X & Y axis Generate 
axis = turtle.Turtle()
axis.color('gray')
axis.pensize(3)
axis.hideturtle()
axis.speed(0)

axis.penup()
axis.goto(-400, 0)
axis.pendown()
axis.goto(400, 0)

axis.penup()
axis.goto(0, -300)
axis.pendown()
axis.goto(0, 300)
axis.penup()

# Take starting & Ending point
x1, y1 = -8, -5
x2, y2 = 8, 6

# Drawing actual line 
actual_line = turtle.Turtle()
actual_line.hideturtle()
actual_line.pensize(1)
actual_line.color('gray')

actual_line.penup()
actual_line.goto(x1*scale, y1*scale)
actual_line.pendown()
actual_line.goto(x2*scale, y2*scale)

# DDA Line Draw
dda_line = turtle.Turtle()
dda_line.hideturtle()

points = ddaLineDrawing(x1, y1, x2, y2)

dda_line.penup()
for x, y in points : 
    dda_line.goto(x*scale, y*scale)
    dda_line.dot(12, 'blue')

    screen.update()
    time.sleep(0.1)




screen.mainloop()