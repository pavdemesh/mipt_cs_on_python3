#!/usr/bin/python3

from pyrob.api import *
import time


@task(delay=0.01)
def task_8_30():
    left_border_reached = False
    right_border_reached = False

    while not (left_border_reached and right_border_reached):
        if not wall_is_beneath():
            move_down()
            # time.sleep(0.2)
            left_border_reached = False
            right_border_reached = False
        elif not right_border_reached:
            if not wall_is_on_the_right():
                move_right()
                # time.sleep(0.05)
            else:
                right_border_reached = True
        else:
            if not wall_is_on_the_left():
                move_left()
                # time.sleep(0.05)
            else:
                left_border_reached = True


if __name__ == '__main__':
    run_tasks()
