#!/usr/bin/python3

from pyrob.api import *


@task
def task_7_5():
    steps_to_move = 1
    move_right()
    fill_cell()
    while not wall_is_on_the_right():
        move_right()
        fill_cell()
        for i in range(steps_to_move):
            if not wall_is_on_the_right():
                move_right()
            elif wall_is_on_the_right():
                continue
        steps_to_move += 1


if __name__ == '__main__':
    run_tasks()
