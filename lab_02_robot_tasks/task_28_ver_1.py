#!/usr/bin/python3

from pyrob.api import *


@task
def task_7_6():
    counter_filled_cells = 0

    while counter_filled_cells < 5:
        move_right()
        if cell_is_filled():
            counter_filled_cells += 1


if __name__ == '__main__':
    run_tasks()
