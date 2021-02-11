import turtle
import math


def fn_draw_circle(direction, radius=60, smooth_factor=70):
    """Will draw a square of size n"""
    rotation_angle = 360 / smooth_factor
    move_distance = 2 * radius * math.pi / smooth_factor
    if direction == "left":
        for _i in range(smooth_factor):
            turtle.forward(move_distance)
            turtle.left(rotation_angle)
    elif direction == "right":
        for _i in range(smooth_factor):
            turtle.forward(move_distance)
            turtle.right(rotation_angle)


def fn_draw_butterfly(number_of_layers=10, start_size=40):
    increment = start_size // 5
    current_size = start_size
    turtle.left(90)
    for _i in range(number_of_layers):
        fn_draw_circle("left", current_size)
        fn_draw_circle("right", current_size)
        current_size += increment
    turtle.penup()
    turtle.forward(250)


turtle.shape("turtle")
fn_draw_butterfly()
turtle.done()
