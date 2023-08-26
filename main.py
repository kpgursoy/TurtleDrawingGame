import turtle

drawing_board = turtle.Screen()
drawing_board.bgcolor("light blue")
drawing_board.title("Python Turtle")
mahmut = turtle.Turtle()


def turtle_forward():
    mahmut.forward(100)


def rotate_angle_right():
    mahmut.setheading(mahmut.heading() - 10)


def rotate_angle_left():
    mahmut.setheading(mahmut.heading() + 10)


def clear_screen():
    mahmut.clear()


def turtle_pen_up():
    mahmut.penup()


def turtle_pen_down():
    mahmut.pendown()


def turtle_return_home():
    mahmut.home()


drawing_board.listen()
drawing_board.onkey(key="space", fun=turtle_forward)
drawing_board.onkey(key="Down", fun=rotate_angle_right)
drawing_board.onkey(key="Up", fun=rotate_angle_left)
drawing_board.onkey(key="c", fun=clear_screen)
drawing_board.onkey(key="q", fun=turtle_pen_up)
drawing_board.onkey(key="w", fun=turtle_pen_down)
drawing_board.onkey(key="h", fun=turtle_return_home)

drawing_board.exitonclick()
# turtle.done()
