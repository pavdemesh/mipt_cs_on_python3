import turtle


def fn_draw_single_whorl(edge_size):
    turtle.forward(edge_size)
    turtle.left(90)
    turtle.forward(edge_size)
    turtle.left(90)


def fn_draw_quadratic_spiral(num_of_whorls=8, start_size=20):
    current_edge = start_size
    for _i in range(num_of_whorls * 2):
        fn_draw_single_whorl(current_edge)
        current_edge += start_size


turtle.shape("turtle")
fn_draw_quadratic_spiral(12, 20)
turtle.done()
