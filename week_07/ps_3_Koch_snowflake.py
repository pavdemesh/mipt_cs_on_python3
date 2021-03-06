import turtle
import time

# Initialize turtle and bring it to start position
turtle.shape("turtle")
turtle.color("purple")
turtle.penup()
turtle.goto(-350, -250)
turtle.pendown()
turtle.speed("fastest")
# End of initialize


def draw_koch_line(length=700.00, depth=1):
    if depth == 1:
        step = length / 3
        turtle.forward(step)
        turtle.left(60)
        turtle.forward(step)
        turtle.right(120)
        turtle.forward(step)
        turtle.left(60)
        turtle.forward(step)
        return

    else:
        step = length / 3
        draw_koch_line(step, depth - 1)
        turtle.left(60)
        draw_koch_line(step, depth - 1)
        turtle.right(120)
        draw_koch_line(step, depth - 1)
        turtle.left(60)
        draw_koch_line(step, depth - 1)


draw_koch_line(700.00, 5)
time.sleep(5)
