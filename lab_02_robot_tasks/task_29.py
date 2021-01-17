#!/usr/bin/python3

from pyrob.api import *


@task
def task_7_7():
    cells_filled_in_row = 0

    while not wall_is_on_the_right() and cells_filled_in_row < 3:
        move_right()
        if cell_is_filled():
            cells_filled_in_row += 1
        elif not cell_is_filled():
            cells_filled_in_row = 0



if __name__ == '__main__':
    run_tasks()
