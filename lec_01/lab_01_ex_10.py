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


def fn_draw_flower(number_of_petals=10, radius_of_petal=80):
    rotation_angle = 360 / number_of_petals
    for _i in range(number_of_petals // 2):
        fn_draw_circle("left", radius_of_petal)
        fn_draw_circle("right", radius_of_petal)
        turtle.left(rotation_angle)
    turtle.penup()
    turtle.forward(200)


turtle.shape("turtle")
fn_draw_flower()
turtle.done()
