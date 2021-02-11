#!/usr/bin/python3

from pyrob.api import *
import time

# from lec_02.pyrob.core import *


@task(delay=0.01)
def task_8_30():
    # Measure length of a row
    length_of_row = 1
    while not wall_is_on_the_left():
        move_left()
        length_of_row += 1
    move_right(length_of_row - 1)

    left_border_reached = False
    right_border_reached = False
    # Testing this stuff
    current_position = 0
    offset_left = 0
    offset_right = 0
    middle_point = length_of_row // 2

    while not (left_border_reached and right_border_reached):
        if not wall_is_beneath():
            move_down()
            # time.sleep(0.2)
            left_border_reached = False
            right_border_reached = False
            current_position = current_position + offset_left - offset_right
            offset_left = 0
            offset_right = 0

        elif current_position <= middle_point and not right_border_reached:
            if not wall_is_on_the_right():
                move_right()
                offset_right += 1
                time.sleep(0.07)
            else:
                right_border_reached = True

        elif current_position <= middle_point and right_border_reached:
            if not wall_is_on_the_left():
                move_left()
                offset_left += 1
                time.sleep(0.07)
            else:
                left_border_reached = True

        elif current_position > middle_point and not left_border_reached:
            if not wall_is_on_the_left():
                move_left()
                offset_left += 1
                time.sleep(0.07)
            else:
                left_border_reached = True

        elif current_position > middle_point and left_border_reached:
            if not wall_is_on_the_right():
                move_right()
                offset_right += 1
                time.sleep(0.07)
            else:
                right_border_reached = True

    while not wall_is_on_the_left():
        move_left()


if __name__ == '__main__':
    run_tasks()
