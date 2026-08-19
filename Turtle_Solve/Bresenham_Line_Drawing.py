import turtle
import time 

scale = 40
def bresenhamLine(x1, y1, x2, y2) : 
    points = []
    dx = abs(x2-x1)
    dy = abs(y2-y1)

    sx = 1 if x1 < x2 else -1
    sy = 1 if y1 < y2 else -1

    err = dx - dy 

    while True : 
        points.append((x1, y1))
        if x1 == x2 and y1 == y2 : 
            break
        
        e2 = 2 * err
        if e2 > -dy : 
            x1 += sx
            err -= dy

        if e2 < dx :
            y1 += sy
            err += dx

    return points


# Turtle setup 
screen = turtle.Screen()
screen.setup(900, 700)
screen.title("Bresenhams Line Drawing Algorithm")
screen.tracer(0)

# X & Y axis generate 
axis = turtle.Turtle()
axis.hideturtle()
axis.color('gray')
axis.pensize(3)
axis.speed(0)

axis.penup()
axis.goto(-400, 0)
axis.pendown()
axis.goto(400, 0)

axis.penup()
axis.goto(0, -300)
axis.pendown()
axis.goto(0, 300)

# Take Staring and Endig Point 
x1,y1 = -3, -3
x2, y2 = 5, 6

# Calculate Points 
points = bresenhamLine(x1, y1, x2, y2)

# Draw True Line 
actual_line = turtle.Turtle()
actual_line.color('black')
actual_line.pensize(2)
actual_line.hideturtle()

actual_line.penup()
actual_line.goto(x1*scale, y1*scale)
actual_line.pendown()
actual_line.goto(x2*scale, y2*scale)

# Draw bresenhams Line 
points = bresenhamLine(x1, y1, x2, y2)
bresenham_line = turtle.Turtle()
bresenham_line.hideturtle()
bresenham_line.speed(0)

bresenham_line.penup()
for x, y in points : 
    bresenham_line.goto(x*scale, y*scale)
    bresenham_line.dot(12, 'red')

    
    screen.update()
    time.sleep(0.3)

screen.mainloop()