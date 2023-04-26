from random import uniform, randint
from tkinter import Tk, Canvas
from math import sin, radians


X = 1000
Y = round(X * sin(radians(60)), 2)
AREA = (X * Y) / 2
TRIANGLE_VERTICES = {1: (0, Y), 2: (X, Y), 3: (X / 2, 0)}


def generate_random_initial_point() -> tuple:
    random_x_coord = round(uniform(0, X), 2)
    random_y_coord = round(uniform(0, Y), 2)
    return (random_x_coord, random_y_coord)


def determine_starting_point() -> tuple:
    random_index = randint(1, 3)
    random_starting_point = TRIANGLE_VERTICES[random_index]
    return random_starting_point


def midpoint(a: tuple, b: tuple) -> tuple:
    average_point = (round((a[0] + b[0]) / 2, 2), round((a[1] + b[1]) / 2, 2))
    return average_point


def area_of_triangle(point_1: tuple, point_2: tuple, point_3: tuple) -> int:
    x1, y1 = point_1[0], point_1[1]
    x2, y2 = point_2[0], point_2[1]
    x3, y3 = point_3[0], point_3[1]
    return abs((x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2)


def is_inside_triangle(
    random_point: tuple, first_point: tuple, second_point: tuple, third_point
) -> bool:
    a1 = area_of_triangle(random_point, second_point, third_point)
    a2 = area_of_triangle(first_point, random_point, third_point)
    a3 = area_of_triangle(first_point, second_point, random_point)
    return AREA == (a1 + a2 + a3)


def generate_random_point() -> tuple:
    while True:
        random_point = generate_random_initial_point()
        if is_inside_triangle(
            random_point,
            TRIANGLE_VERTICES[1],
            TRIANGLE_VERTICES[2],
            TRIANGLE_VERTICES[3],
        ):
            break

    return random_point


root = Tk()
root.title("Sierpinski's Triangle")
canvas = Canvas(root, width=X, height=Y, bg="#000000")
canvas.pack()

random_point = generate_random_point()
for _ in range(100000):
    canvas.create_rectangle(random_point * 2, outline="teal")
    random_starting_point = determine_starting_point()
    average_point = midpoint(random_point, random_starting_point)
    random_point = average_point

root.mainloop()