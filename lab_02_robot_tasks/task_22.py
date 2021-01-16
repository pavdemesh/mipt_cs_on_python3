#!/usr/bin/python3

from pyrob.api import *


@task
def task_5_10():
    num_rows = 1
    num_cols = 1

    while not wall_is_on_the_right():
        move_right()
        num_cols += 1

    while not wall_is_beneath():
        move_down()
        num_rows += 1

    for i in range(num_cols):
        for j in range(num_rows):
            fill_cell()
            if not wall_is_above():
                move_up()
        try:
            move_down(num_rows - 1)
        except:
            fill_cell()
        if not wall_is_on_the_left():
            move_left()


if __name__ == '__main__':
    run_tasks()
