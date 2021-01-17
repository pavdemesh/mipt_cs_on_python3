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
def task_2_1():

    move_down(2)
    move_right()
    fn_draw_cross()
    fn_move_finish()


if __name__ == '__main__':
    run_tasks()
