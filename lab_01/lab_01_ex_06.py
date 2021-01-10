import turtle
# import time


def fn_draw_leg(len_of_leg):
    turtle.forward(len_of_leg)
    turtle.stamp()
    turtle.penup()
    turtle.left(180)
    turtle.forward(len_of_leg)
    turtle.pendown()


def fn_draw_spider(num_of_legs=12, len_of_leg=150):
    rotation_angle = 360 / num_of_legs
    for _i in range(num_of_legs):
        fn_draw_leg(len_of_leg)
        turtle.left(rotation_angle)
        # time.sleep(2)


turtle.shape("turtle")
turtle.speed(1)
fn_draw_spider()
turtle.done()
