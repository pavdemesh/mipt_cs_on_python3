import graphics as gr

window = gr.GraphWin("Jenkslex and Ganzz project", 800, 800)


def draw_sky():
    sky = gr.Rectangle(gr.Point(0, 400), gr.Point(800, 0))
    sky.setFill("blue")
    sky.draw(window)


def draw_sun(x, y, radius):
    sun = gr.Circle(gr.Point(x, y), radius)
    sun.setFill("yellow")
    sun.draw(window)


def draw_cloud(x, y, radius):
    y_temp = y - radius
    horizontal_move = radius // 2
    for _ in range(2):
        cloud_part = gr.Circle(gr.Point(x + horizontal_move, y_temp), radius)
        cloud_part.setFill("white")
        cloud_part.draw(window)
        horizontal_move += radius

    horizontal_move = 0
    for _ in range(3):
        cloud_part = gr.Circle(gr.Point(x + horizontal_move, y), radius)
        cloud_part.setFill("white")
        cloud_part.draw(window)
        horizontal_move += radius


def draw_christmas_tree(x, y, height):
    tree_step = height / 11
    tree_stem_length = tree_step * 4

    def draw_stem(x_start, y_start, x_end, y_end):
        tree_stem = gr.Line(gr.Point(x_start, y_start), gr.Point(x_end, y_end))
        tree_stem.setWidth(25)
        tree_stem.setOutline("brown")
        tree_stem.draw(window)

    def draw_triangle(x_, y_, height_):
        green_triangle = gr.Polygon(gr.Point(x_, y_), gr.Point(x_ + height_, y_ + height_),
                                    gr.Point(x_ - height_, y_ + height_))
        green_triangle.setFill("green")
        green_triangle.draw(window)

    draw_stem(x, y + height - tree_stem_length, x, y + height)

    for i in range(3):
        draw_triangle(x, y + 4 * tree_step, 3 * tree_step)
        y = y - 2 * tree_step


def draw_house(x, y, height, width):
    # Draw house body
    house_body = gr.Rectangle(gr.Point(x, y), gr.Point(x + width, y - height))
    house_body.setFill("gray")
    house_body.draw(window)

    # Draw house roof
    roof = gr.Polygon(gr.Point(x, y - height), gr.Point(x + width, y - height),
                      gr.Point(x + width / 2, y - height - width / 2))
    roof.setFill("red")
    roof.draw(window)

    # Draw window
    house_window = gr.Rectangle(gr.Point(x + width / 3, y - height / 3),
                                gr.Point(x + width / 3 * 2, y - height / 3 * 2))
    house_window.setFill("yellow")
    house_window.draw(window)

    # Draw window cross
    window_vertical_line = gr.Line(gr.Point(x + width / 2, y - height / 3), gr.Point(x + width / 2, y - height / 3 * 2))
    window_horizontal_line = gr.Line(gr.Point(x + width / 3, y - height / 2), gr.Point(x + width / 3 * 2, y - height / 2))

    window_vertical_line.setWidth(7)
    window_horizontal_line.setWidth(7)

    window_horizontal_line.draw(window)
    window_vertical_line.draw(window)


draw_sky()
draw_sun(700, 100, 75)
draw_cloud(75, 100, 25)
draw_cloud(350, 75, 35)
draw_cloud(500, 150, 25)
draw_christmas_tree(625, 375, 350)
draw_house(125, 600, 300, 300)

window.getMouse()
window.close()
