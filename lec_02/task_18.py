#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_28():
    counter_steps = 1
    exit_found = False
    while not exit_found:
        if not wall_is_above():
            move_up()
            exit_found = True
            break
        if not wall_is_on_the_left():
            move_left()
            counter_steps += 1
        else:
            move_right(counter_steps)
            break

    while not exit_found:
        if not wall_is_above():
            move_up()
            exit_found = True
            break
        if not wall_is_on_the_right():
            move_right()

    while not wall_is_on_the_left():
        move_left()
    while not wall_is_above():
        move_up()


if __name__ == '__main__':
    run_tasks()
