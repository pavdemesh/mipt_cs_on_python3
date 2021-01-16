#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.05)
def task_4_3():
    # Flag to control direction left to right or vice versa
    left_to_right = True
    # Move right onto the first cell to be filled
    move_right()
    # For every row (total 12 rows)
    for _i in range(12):

        # If direction flag is True - fill left to right
        if left_to_right:
            for _j in range(27):
                fill_cell()
                move_right()
            # Move to first cell in the next row
            move_left()
            move_down()
            # After finished filling the row - reverse the value of direction flag
            left_to_right = not left_to_right

        # If direction flag is False - fill right to left
        elif not left_to_right:
            for _j in range(27):
                fill_cell()
                move_left()
            # Return to first cell in the next row
            move_right()
            move_down()
            left_to_right = not left_to_right
    # Last filling fill be right to left. So that the return moves of the last call of r-to-l branch
    # Will bring the robot to its destination.


if __name__ == '__main__':
    run_tasks()
