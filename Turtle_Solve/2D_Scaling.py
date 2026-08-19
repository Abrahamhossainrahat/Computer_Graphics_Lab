import turtle
import time


# --------------------------------
# Screen Setup
# --------------------------------
screen = turtle.Screen()
screen.setup(900, 700)
screen.title("2D Translation Animation")
screen.tracer(0)


scale = 40


# --------------------------------
# Draw X and Y Axis
# --------------------------------
axis = turtle.Turtle()
axis.hideturtle()
axis.speed(0)
axis.color("gray")

axis.penup()
axis.goto(-400, 0)
axis.pendown()
axis.goto(400, 0)

axis.penup()
axis.goto(0, -300)
axis.pendown()
axis.goto(0, 300)


# --------------------------------
# Polygon Drawing Function
# --------------------------------
def draw_polygon(pen, points):

    pen.clear()

    pen.penup()

    x, y = points[0]
    pen.goto(x * scale, y * scale)

    pen.pendown()

    for x, y in points[1:]:
        pen.goto(x * scale, y * scale)

    # polygon close
    x, y = points[0]
    pen.goto(x * scale, y * scale)

    pen.penup()


# --------------------------------
# Original Triangle
# --------------------------------
triangle = [
    (-3, -2),
    (0, 3),
    (3, -2)
]


# Translation amount
sx = 2
sy = 1.5


# --------------------------------
# Original Object
# --------------------------------
original_pen = turtle.Turtle()
original_pen.hideturtle()
original_pen.speed(0)
original_pen.color("red")
original_pen.pensize(3)

draw_polygon(original_pen, triangle)


# --------------------------------
# Moving Object
# --------------------------------
moving_pen = turtle.Turtle()
moving_pen.hideturtle()
moving_pen.speed(0)
moving_pen.color("blue")
moving_pen.pensize(4)


# --------------------------------
# Translation Animation
# --------------------------------
steps = 60

for i in range(steps + 1):

    t = i / steps
    current_sx = 1 + (sx-1)*t
    current_sy = 1 + (sy-1)*t
    current_points = []

    for x, y in triangle:

        new_x = x * current_sx
        new_y = y * current_sy

        current_points.append(
            (new_x, new_y)
        )

    draw_polygon(
        moving_pen,
        current_points
    )

    screen.update()

    time.sleep(0.03)


screen.mainloop()