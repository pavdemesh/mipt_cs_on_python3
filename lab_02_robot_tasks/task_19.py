#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_29():
    counter_steps = 1
    exit_found = False

    while wall_is_above() and wall_is_beneath() and not wall_is_on_the_left():
        move_left()
        counter_steps += 1
    else:
        if not wall_is_above():
            exit_found = True
            move_up()
        else:
            move_right(counter_steps)

    if not exit_found:
        while wall_is_above() and wall_is_beneath() and not wall_is_on_the_right():
            move_right()
        else:
            if not wall_is_above():
                exit_found = True
                move_up()

    while exit_found and not wall_is_on_the_left():
        move_left()
    while exit_found and not wall_is_above():
        move_up()


if __name__ == '__main__':
    run_tasks()
