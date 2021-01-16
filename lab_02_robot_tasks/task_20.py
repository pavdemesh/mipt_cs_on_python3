#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.05)
def task_4_3():
    move_right()
    # Переменной dx присваивается значение 1
    # Переменной dy присваивается значение 0
    # Обычно dx и dy - это некие приращения для переменных x и y
    dx, dy = 1, 0

    # Переменным x и y присваивается значение 0
    x, y = 0, 0

    change_direction = False

    # Выполняется перебор
    # Для переменной i последовательно перебираем значения от 1 до (rows * cols)
    for i in range(12 * 27):
        # Элемент матрицы с координатами x и y закрашивается
        # print(f"dx = {dx} and dy = {dy}")
        # print(f"x = {x} and y = {y}")
        fill_cell()
        change_direction = False
        # Создаются временные переменные nx и ny
        # в которых вычисляются новые значения для x и y
        # для этого к старым значенииям прибавляются приращения
        nx, ny = x + dx, y + dy
        # Если всё нормально, и индекс не выскочил за пределы матрицы
        # или не наткнулся на уже закрашенную ячейку
        if 0 <= nx <= 26 and 0 <= ny <= 11:
            if dx == 1 and dy == 0:
                move_right()
                if not cell_is_filled():
                    x, y = nx, ny
                    continue
                else:
                    change_direction = True
                move_left()
            elif dx == -1 and dy == 0:
                move_left()
                if not cell_is_filled():
                    x, y = nx, ny
                    continue
                else:
                    change_direction = True
                move_right()
            elif dx == 0 and dy == 1:
                move_down()
                if not cell_is_filled():
                    x, y = nx, ny
                    continue
                else:
                    change_direction = True
                move_up()
            elif dx == 0 and dy == -1:
                move_up()
                if not cell_is_filled():
                    x, y = nx, ny
                    continue
                else:
                    change_direction = True
                move_down()
            # то эти значения и оставляются

        if change_direction:
            dx, dy = -dy, dx
            # и используем уже это изменённое движение для новых значений x и y
            x, y = x + dx, y + dy

        if not (0 <= nx <= 26 and 0 <= ny <= 11):
            # а если индекс выскочил за границу матрицы
            # или наткнулся на уже занятую ячейку
            # то разворачиваемся на 90 градусов
            # путем замены приращения по x и y друг на друга
            # а минус нужен, чтобы он не ходил только вправо или вниз,
            # а чередовал с движениями вверх или влево.
            # Так и получается спираль
            dx, dy = -dy, dx
            # и используем уже это изменённое движение для новых значений x и y
            x, y = x + dx, y + dy

        # Определяем направление движения на основании приращений
        if dx == 1 and dy == 0:
            move_right()
        elif dx == -1 and dy == 0:
            move_left()
        elif dx == 0 and dy == 1:
            move_down()
        elif dx == 0 and dy == -1:
            move_up()

    move_down(7)
    move_left(5)


if __name__ == '__main__':
    run_tasks()
