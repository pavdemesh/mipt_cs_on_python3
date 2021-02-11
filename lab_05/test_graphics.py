import graphics as gr
import time


window = gr.GraphWin("Model", 800, 800)
coords = gr.Point(400, 400)
velocity = gr.Point(2, 3)

circle = gr.Circle(coords, 10)
circle.setFill('red')
circle.draw(window)

test_circle = gr.Circle(gr.Point(600, 600), 30)
test_circle.setFill("green2")
test_circle.draw(window)


def update_coords(coords_, velocity_):
    new_coords = gr.Point(coords_.x + velocity_.x,
                          coords_.y + velocity_.y)
    return new_coords


def update_velocity(coords_, velocity_):
    if coords_.x < 0 or coords_.x > 800:
        velocity_.x = - velocity_.x
    if coords_.y < 0 or coords_.y > 800:
        velocity_.y = - velocity_.y
    return velocity_


while True:
    circle.move(velocity.x, velocity.y)
    print(coords.y)
    coords = update_coords(coords, velocity)
    velocity = update_velocity(coords, velocity)
    time.sleep(0.02)

window.getMouse()
window.close()
