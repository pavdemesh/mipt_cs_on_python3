#!/usr/bin/python3

from pyrob.api import *


@task
def task_5_10():
    # Just in case that we have 1x1 grid
    # fill_cell()
    # Create boolean variable to track direction
    left_to_right = True

    # Repeat until bottom is reached
    while not wall_is_beneath():
        fill_cell()
        # If left to right is True: fill left to right
        if left_to_right:
            while not wall_is_on_the_right():
                move_right()
                fill_cell()
            # Change direction
            left_to_right = not left_to_right
        # If left to right is False: fill right to left
        elif not left_to_right:
            while not wall_is_on_the_left():
                move_left()
                fill_cell()
            # Change direction
            left_to_right = not left_to_right
        move_down()

    # Now let's fill the last row
    if not left_to_right:
        fill_cell()
        while not wall_is_on_the_left():
            move_left()
            fill_cell()
    else:
        fill_cell()
        while not wall_is_on_the_right():
            move_right()
            fill_cell()
        while not wall_is_on_the_left():
            move_left()


if __name__ == '__main__':
    run_tasks()
