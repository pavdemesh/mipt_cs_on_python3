#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_29():
    counter_steps = 1
    exit_found = False
    left_border_reached = False
    right_border_reached = False

    while not exit_found and not left_border_reached:
        if not wall_is_above():
            exit_found = True
            continue
        elif not wall_is_on_the_left():
            move_left()
            counter_steps += 1
        else:
            left_border_reached = True
            move_right(counter_steps)

    if left_border_reached:
        while not exit_found and not right_border_reached:
            if not wall_is_above():
                exit_found = True
                continue
            elif not wall_is_on_the_right():
                move_right()
            else:
                right_border_reached = True

    if exit_found:
        while not wall_is_above():
            move_up()
        while not wall_is_on_the_left():
            move_left()


if __name__ == '__main__':
    run_tasks()
