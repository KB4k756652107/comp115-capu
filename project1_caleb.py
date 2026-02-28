import turtle as t
import time

screen = t.Screen()
screen.bgcolor("#38E8FF")
screen.tracer(0)
tracy = t.Turtle()
tracy.speed(0)
tracy.setheading(90)
# tracy.penup()
tracy.pencolor("#2F2F2F")
tracy.pensize(1)
tracy.hideturtle()
pos_1 = {}
pos_2 = {}


def stick():
    tracy.fillcolor("#ffe600")
    heading = tracy.heading()
    tracy.setheading(0)
    tracy.forward(4)

    for _ in range(2):
        tracy.begin_fill()
        tracy.right(90)
        tracy.forward(550)
        tracy.right(90)
        tracy.forward(8)
        tracy.end_fill()
    tracy.goto(0, 0)
    tracy.setheading(heading)


def flap():
    tracy.fillcolor("#0013e6")

    for i in range(4):
        tracy.begin_fill()
        tracy.forward(250)
        tracy.left(45)
        tracy.forward(-120)
        pos_1[i] = tracy.position()
        tracy.circle(50, -45, 50)
        pos_2[i] = tracy.position()
        tracy.forward(-130)
        tracy.goto(0, 0)
        tracy.end_fill()
        tracy.right(90)

def fold():
    tracy.fillcolor("#162aff")

    for i in range(4):
        tracy.begin_fill()
        tracy.goto(pos_2[i][0], pos_2[i][1])
        tracy.forward(-130)
        tracy.circle(1, -45, 1)
        tracy.circle(86.85, -45, 87)
        tracy.goto(0, 0)
        tracy.end_fill()

def pin():
    tracy.fillcolor("#000000")
    tracy.right(90)
    tracy.forward(6)
    tracy.left(90)
    tracy.begin_fill()
    tracy.circle(6, 360, 180)
    tracy.end_fill()
    tracy.penup()
    tracy.goto(0, 0)
    tracy.pendown()

def pinwheel():
    stick()
    flap()
    fold()
    pin()

while(1):
    pinwheel()
    tracy.right(5)
    screen.update()
    time.sleep(0.01)
    tracy.clear()

screen.mainloop()




# tracy.fillcolor("#0a1ef3")

# for i in range(4):
#     tracy.begin_fill()
#     tracy.goto(pos_1[i][0], pos_1[i][1])
#     tracy.left(45)
#     tracy.circle(50, -45, 50)
#     tracy.forward(-130)
#     tracy.goto(0, 0)
#     tracy.right(90)
#     tracy.end_fill()