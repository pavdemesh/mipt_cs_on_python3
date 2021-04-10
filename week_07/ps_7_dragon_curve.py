import turtle
import time
import math


# Initialize turtle and bring it to start position
turtle.shape("turtle")
turtle.color("green")
turtle.penup()
turtle.goto(-150, -150)
turtle.pendown()
turtle.speed("fast")
# End of initialize


def draw_dragon_curve(length=300.00, depth=1):
    if depth == 1:
        step = length / 2 / math.cos(45 * math.pi / 180)
        turtle.right(45)
        turtle.forward(step)
        turtle.left(90)
        turtle.forward(step)
        return

    else:
        step = length / 2 / math.cos(45 * math.pi / 180)
        turtle.right(45)
        draw_dragon_curve(step, depth - 1)
        turtle.left(45)
        draw_dragon_curve(step, depth - 1)


draw_dragon_curve(300.00, 2)
time.sleep(5)
