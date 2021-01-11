import turtle
import math


def fn_draw_arch(radius=50, smooth_factor=30):
    """Will draw a square of size n"""
    rotation_angle = 180 / smooth_factor
    move_distance = radius * math.pi / smooth_factor
    for _i in range(smooth_factor):
        turtle.forward(move_distance)
        turtle.right(rotation_angle)


def fn_draw_spring(number_of_arches=10, spring_size=50):
    turtle.penup()
    turtle.goto(-300, 0)
    turtle.pendown()
    big_arch = spring_size
    small_arch = spring_size // 5
    turtle.left(90)
    for _i in range(number_of_arches):
        fn_draw_arch(big_arch)
        fn_draw_arch(small_arch)


turtle.shape("turtle")
turtle.speed(9)
fn_draw_spring()
turtle.done()
