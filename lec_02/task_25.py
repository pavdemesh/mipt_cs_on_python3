#!/usr/bin/python3

from pyrob.api import *


def fn_draw_cross():
    fill_cell()
    move_right()
    fill_cell()
    move_up()
    fill_cell()
    move_down(2)
    fill_cell()
    move_up()
    move_right()
    fill_cell()


def fn_move_finish():
    move_left(2)
    move_up()


@task
def task_2_2():
    move_down(2)
    while not wall_is_on_the_right():
        fn_draw_cross()
        if not wall_is_on_the_right():
            move_right(2)

    fn_move_finish()

if __name__ == '__main__':
    run_tasks()
