import turtle


def fn_draw_square(n):
    """Will draw a square of size n"""
    turtle.shape('turtle')
    for i in range(4):
        turtle.forward(n)
        turtle.left(90)
    turtle.done()


fn_draw_square(200)

