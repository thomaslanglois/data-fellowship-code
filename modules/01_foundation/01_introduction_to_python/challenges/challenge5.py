import turtle


def draw_square(turtle, size):
    for i in range(4):
        turtle.forward(size)
        turtle.left(90)


def draw_shape(turtle, sides, length):
    for i in range(sides):
        turtle.forward(length)
        turtle.right(360/sides)


if __name__ == "__main__":
    t = turtle.Turtle()
    t.speed(0)
    window = turtle.Screen()

    """ draw a triangle """
    for i in range(3):
        t.forward(100)
        t.left(120)

    """ draw a square inside a triangle inside a circle """
    t.penup()
    t.right(300)
    t.forward(200)
    t.pendown()

    """ draw a circle """
    for i in range(360):
        t.forward(2)
        t.left(1)

    """ draw a triangle inside the circle """
    t.penup()
    t.left(45)
    t.forward(50)
    t.pendown()
    for i in range(3):
        t.forward(100)
        t.left(120)

    """ draw a square inside the triangle """
    t.penup()
    t.left(20)
    t.forward(50)
    t.pendown()
    for i in range(4):
        t.forward(20)
        t.left(90)

    """ test draw_square """
    t.penup()
    t.left(45)
    t.forward(200)
    t.pendown()

    draw_square(t, 55)

    """ test draw_shape """
    t.penup()
    t.left(45)
    t.forward(200)
    t.pendown()

    draw_shape(t, 12, 20)

    window.exitonclick()
