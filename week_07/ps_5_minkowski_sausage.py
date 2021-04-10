import turtle
import time

# Initialize turtle and bring it to start position
turtle.shape("turtle")
turtle.color("green")
turtle.penup()
turtle.goto(-350, 0)
turtle.pendown()
turtle.speed("fast")
# End of initialize


def draw_minkowski(length=700.00, depth=1):
    if depth == 1:
        step = length / 4
        turtle.forward(step)
        turtle.left(90)
        turtle.forward(step)
        turtle.right(90)
        turtle.forward(step)
        turtle.right(90)
        turtle.forward(step)
        turtle.forward(step)
        turtle.left(90)
        turtle.forward(step)
        turtle.left(90)
        turtle.forward(step)
        turtle.right(90)
        turtle.forward(step)
        return

    else:
        step = length / 4
        draw_minkowski(step, depth - 1)
        turtle.left(90)
        draw_minkowski(step, depth - 1)
        turtle.right(90)
        draw_minkowski(step, depth - 1)
        turtle.right(90)
        draw_minkowski(step, depth - 1)
        draw_minkowski(step, depth - 1)
        turtle.left(90)
        draw_minkowski(step, depth - 1)
        turtle.left(90)
        draw_minkowski(step, depth - 1)
        turtle.right(90)
        draw_minkowski(step, depth - 1)


draw_minkowski(700, 3)
time.sleep(5)
