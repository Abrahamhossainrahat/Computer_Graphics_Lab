import turtle 
import time 

# Turtle setup 
screen = turtle.Screen()
screen.setup(1000, 700)
screen.title("Deterministic Self Similar Fractral Curve")
screen.tracer(0)

# fractral draw
fractral = turtle.Turtle()
fractral.pensize(3)
fractral.color('red')
fractral.speed(0)

fractral.penup()
fractral.goto(-200, 0)
fractral.pendown()

def self_similar(len, order) :
    if order == 0 :
        fractral.forward(len)
        screen.update()
        time.sleep(0.01)

    else : 
        self_similar(len/3, order-1)
        fractral.left(60)

        self_similar(len/3, order-1)
        fractral.right(120)

        self_similar(len/3, order-1)
        fractral.left(60)

        self_similar(len/3, order-1)

def snowflake(len, order) :
    for _ in range(3) :
        self_similar(len, order)
        fractral.right(120)

length = 400
order = 4
snowflake(length, order)

screen.update()
screen.mainloop()