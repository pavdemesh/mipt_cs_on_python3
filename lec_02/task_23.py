#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_6_6():
    counter_right_steps = 0
    counter_up_steps = 0

    while not wall_is_on_the_right():
        move_right()
        counter_right_steps += 1

        if not wall_is_above():
            while not wall_is_above():
                move_up()
                counter_up_steps += 1
                fill_cell()
            move_down(counter_up_steps)
            counter_up_steps = 0

    move_left(counter_right_steps)


if __name__ == '__main__':
    run_tasks()
