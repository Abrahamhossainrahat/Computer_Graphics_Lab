import turtle
import time 

scale = 30
inside = 0
left = 1
right = 2
bottom = 4
top = 8

def outcode_generate(x, y, xmin, ymin, xmax, ymax) : 
    code = inside

    if x < xmin : 
        code |= left
    elif x > xmax :
        code |= right

    if y < ymin :
        code |= bottom
    elif y > ymax :
        code |= top

    return code 

# Cohen Sutterland Calculation 

def cohenSutterlandLine(x1, y1, x2, y2, xmin, ymin, xmax, ymax) : 
    points = []

    code1 = outcode_generate(x1, y1, xmin, ymin, xmax, ymax)
    code2 = outcode_generate(x2, y2, xmin, ymin, xmax, ymax)
    m = (y2 - y1)/(x2 - x1)

    points.append((x1, y1, x2, y2))

    while True : 
        if not (code1 | code2) :
            return True, points
        elif (code1 & code2) :
            return False, points
        else : 
            if code1 != 0 :
                outcode = code1
            else : 
                outcode = code2

            if outcode & top :
                x = x1 + (ymax - y1)/m
                y = ymax
            elif outcode & bottom : 
                x = x1 + (ymin - y1)/m
                y = ymin
            elif outcode & right :
                x = xmax
                y = y1 + (xmax - x1)*m
            elif outcode & left : 
                x = xmin
                y = y1 + (xmin-x1)*m

            if outcode == code1 :
                x1, y1 = x, y
                code1 = outcode_generate(x1, y1, xmin, ymin, xmax, ymax)
            else :
                x2, y2 = x, y
                code2 = outcode_generate(x2, y2, xmin, ymin, xmax, ymax)
            
            points.append((x1, y1, x2, y2))


# Turtle setup 
screen = turtle.Screen()
screen.setup(900,700)
screen.title("Cohen Sutterland ALgorithm")
screen.tracer(0)

# Take Input Window and Line
x1, y1 = -8, 5
x2, y2 = 8, -4

xmin, ymin = -4, -3
xmax, ymax = 4, 3

# Drawing Window
window = turtle.Turtle()
window.color('black')
window.pensize(3)
window.hideturtle()
window.speed(0)

window.penup()
window.goto(xmin*scale, ymin*scale)
window.pendown()
window.goto(xmax*scale, ymin*scale)
window.goto(xmax*scale, ymax*scale)
window.goto(xmin*scale, ymax*scale)
window.goto(xmin*scale, ymin*scale)

# Drawing Line
line = turtle.Turtle()
line.color('red')
line.pensize(2)
line.hideturtle()

line.penup()
line.goto(x1*scale, y1*scale)
line.pendown()
line.goto(x2*scale, y2*scale)

# Cohen Sutterland line 
cohen_sutterland_line = turtle.Turtle()
cohen_sutterland_line.hideturtle()
cohen_sutterland_line.pensize(5)

accepted, points = cohenSutterlandLine(x1, y1, x2, y2, xmin, ymin, xmax, ymax)

for x1, y1, x2, y2 in points :
    cohen_sutterland_line.clear()
    cohen_sutterland_line.color('green')
    cohen_sutterland_line.penup()
    cohen_sutterland_line.goto(x1*scale, y1*scale)
    cohen_sutterland_line.pendown()
    cohen_sutterland_line.goto(x2*scale, y2*scale)

    screen.update()
    time.sleep(1)

if accepted :
    x1, y1, x2, y2 = points[-1]
    cohen_sutterland_line.clear()
    cohen_sutterland_line.color('blue')
    cohen_sutterland_line.penup()
    cohen_sutterland_line.goto(x1*scale, y1*scale)
    cohen_sutterland_line.pendown()
    cohen_sutterland_line.goto(x2*scale, y2*scale)

    print("Line accepted")
    print("clipped Line : ", (x1, y1), "to", (x2, y2))

else : 
    cohen_sutterland_line.clear()
    print("Line Rejected")

screen.update()
screen.mainloop()