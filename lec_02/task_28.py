#!/usr/bin/python3

from pyrob.api import *


@task
def task_7_6():
    counter_filled_cells = 0

    while not wall_is_on_the_right():
        move_right()
        if cell_is_filled():
            counter_filled_cells += 1
        if counter_filled_cells == 5:
            break


if __name__ == '__main__':
    run_tasks()
