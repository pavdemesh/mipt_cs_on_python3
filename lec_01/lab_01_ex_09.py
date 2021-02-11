import turtle
import math


def fn_draw_polygon(radius, number_of_edges):
    """Will draw a square of size n"""
    rotation_angle = 360 / number_of_edges
    move_distance = radius * 2 * math.sin(360 / (2 * number_of_edges) * math.pi / 180)
    print(move_distance)
    turtle.shape('turtle')
    half_angle = 180 - 180 * (number_of_edges - 2) / number_of_edges / 2
    turtle.left(half_angle)
    for _i in range(number_of_edges):
        turtle.forward(move_distance)
        turtle.left(rotation_angle)
    turtle.right(half_angle)


actual_radius = 50
actual_number_of_edges = 3
x, y = 0, 0
increment = 35

for i in range(10):
    fn_draw_polygon(actual_radius, actual_number_of_edges)
    turtle.penup()
    x += increment
    turtle.goto(x, y)
    turtle.pendown()
    actual_number_of_edges += 1
    actual_radius += increment

# print(50 / (2 * math.sin(60 * math.pi / 180)))
# fn_draw_polygon(50, 3)

turtle.done()
