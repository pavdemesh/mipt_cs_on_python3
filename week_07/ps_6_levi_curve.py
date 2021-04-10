import turtle
import time
import math


# Initialize turtle and bring it to start position
turtle.shape("turtle")
turtle.color("green")
turtle.penup()
turtle.goto(-150, -150)
turtle.pendown()
turtle.speed("fastest")
# End of initialize


def draw_levi_curve(length=300.00, depth=1):
    if depth == 1:
        step = length / 2 / math.cos(45 * math.pi / 180)
        turtle.left(45)
        turtle.forward(step)
        turtle.right(90)
        turtle.forward(step)
        turtle.left(45)
        return

    else:
        step = length / 2 / math.cos(45 * math.pi / 180)
        turtle.left(45)
        draw_levi_curve(step, depth - 1)
        turtle.right(90)
        draw_levi_curve(step, depth - 1)
        turtle.left(45)


draw_levi_curve(300, 7)
time.sleep(5)
