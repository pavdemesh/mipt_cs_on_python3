import turtle


def fn_draw_square(square_size):
    """Will draw a square of size n"""
    turtle.shape('turtle')
    turtle.speed(3)
    for _ in range(4):
        turtle.forward(square_size)
        turtle.left(90)


def fn_draw_n_squares(n, first_square_size=50, increment=20):
    # Define a func to draw a single circle
    movement_size = first_square_size
    x, y = 0, 0
    turtle.speed(3)
    # Repeat n times:
    for i in range(n):
        # Draw a square of given size
        fn_draw_square(movement_size)
        # Pen up
        turtle.penup()
        # Calculate new coordinates for start
        x -= increment
        y -= increment
        # Go to new coordinates
        turtle.goto(x, y)
        # Pen down
        turtle.pendown()
        # Calculate new movement_size for the square
        movement_size += 2 * increment
    turtle.shape("arrow")
    turtle.done()


fn_draw_n_squares(10)
