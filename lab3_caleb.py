import turtle

drawing = turtle.Screen()
tracy = turtle.Turtle()

def draw_hexagon():
    tracy.speed(5)
    tracy.circle(100, 360, 6)
    drawing.mainloop

def draw_rainbow():
    drawing.clearscreen()
    tracy.speed(0)
    tracy.setheading(90)
    starting_point = 200
    pensize = 15
    radius = 200
    rainbow_colours = ["purple", "blue", "skyblue", "green", "yellow", "orange", "red"]

    for i in range(7):
        tracy.penup()
        tracy.pensize(pensize)
        tracy.goto(starting_point + 15*i, -50)
        tracy.color(rainbow_colours[i])
        tracy.pendown()
        tracy.circle(radius + 15*i, 180)
        tracy.right(180)

    drawing.mainloop()

draw_hexagon()
draw_rainbow()