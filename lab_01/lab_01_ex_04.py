import turtle
import math


def fn_draw_circle(radius=150, smooth_factor=10):
    """Will draw a square of size n"""
    rotation_angle = 360 / smooth_factor
    move_distance = 2 * radius * math.pi / smooth_factor
    turtle.shape('turtle')
    turtle.speed(9)
    for _i in range(smooth_factor):
        turtle.forward(move_distance)
        turtle.left(rotation_angle)
    turtle.done()


fn_draw_circle(radius=150, smooth_factor=40)
