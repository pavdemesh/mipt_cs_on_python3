#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.05)
def task_4_11():
    move_right()
    for i in range(13):
        # print(f"i = {i}")
        for j in range(13 - i):
            move_down()
            fill_cell()
        # print(f"j = {j}")
        if j > 0:
            move_up(j)
        elif j == 0:
            move_left(12)
            move_down()
            continue
        move_right()


if __name__ == '__main__':
    run_tasks()
