#!/usr/bin/python3

from pyrob.api import *
import time


@task(delay=0.01)
def task_9_3():
    # Measure one side of the square and return to start point
    size_of_field = 1
    while not wall_is_on_the_right():
        move_right()
        size_of_field += 1
    move_left(size_of_field - 1)

    # Iterate over each row from right to left
    # Fill all cells in every row with one exception:
    # If (row_index = col_index) or (row_index + col_index + 1 == size of square): NOT fill
    # Move down and return to left start of new row
    for row_num in range(size_of_field):
        for col_num in range(size_of_field):
            if col_num == row_num or (col_num + row_num + 1 == size_of_field):
                pass
            else:
                fill_cell()
            if not wall_is_on_the_right():
                move_right()
                # time.sleep(0.1)
        move_left(size_of_field - 1)
        if not wall_is_beneath():
            move_down()


if __name__ == '__main__':
    run_tasks()
