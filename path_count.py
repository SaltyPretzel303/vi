from turtle import *
from tkinter import *

dim = 6

moves = [(-1, 0), (+1, 0), (0, -1), (0, +1)]


def in_bounds(field):
    return field[0] >= 0 and field[0] < dim and field[1] >= 0 and field[1] < dim


def get_next(field):
    return list(filter(lambda f: in_bounds(f), map(lambda m: (field[0]+m[0], field[1]+m[1]), moves)))


def print_path_prev(prevs):
    for i in range(0, dim):
        for j in range(0, dim):
            if (i, j) in prevs:
                print("X", end=' ')
            else:
                print(" ", end=' ')
        print(' ')

    print("|||||||||||||||||||||||||||||||")


def print_path(path):
    print(f"p: {path}")
    for i in range(0, dim):
        for j in range(0, dim):
            if (i, j) in path:
                print("X", end=' ')
            else:
                print(" ", end=' ')
        print(' ')

    print("|||||||||||||||||||||||||||||||")


factor = 50
start_pos = (-100, 100)


def print_path_file(path, count):
    penup()
    setpos(start_pos)

    coords = list(map(lambda x: (
        x[1]*factor+start_pos[0], (-1)*x[0]*factor+start_pos[1]), path))
    pendown()
    for field in coords:
        setpos(field)

    f_path = f"images/img_{count}.eps"
    getscreen().getcanvas().postscript(file=f_path)

    clear()


def form_path(prevs, start):
    path = []
    current = start
    while current is not None:
        path.append(current)
        current = prevs[current]

    return list(reversed(path))


def count_paths_rec(start_field, end_field, path=[], count=0):
    # print(f"on: {start_field}")
    # print_path(path)

    if start_field == end_field:
        # print("\t\tFOUND\t\t")
        # print_path_file(path, count+1)
        return count + 1

    next_fields = get_next(start_field)
    branches = list(filter(lambda f: f not in path, next_fields))
    # print(f"->: {branches}")

    for b in branches:
        count = count_paths_rec(b, end_field, path + [b], count)

    return count


def count_paths(start_field, end_field):

    path = []
    count = 0
    prevs = {}

    next_fields = [start_field]
    prevs[start_field] = None

    while len(next_fields) > 0:
        current = next_fields.pop()
        print(f"c: {current}")

        if current == end_field:
            print("END")
            print_path(form_path(prevs, current))
            count += 1
        else:
            # path.append(current)

            temp_path = form_path(prevs, current)

            nexts = get_next(current)
            branches = list(filter(lambda b: b not in temp_path, nexts))

            for b in branches:
                prevs[b] = current

            next_fields += branches

            print(f"n: {branches}")

        print_path(form_path(prevs, current))
        a = input("enter")

    return count


# print(count_paths((0, 0), (dim-1, dim-1)))
print(count_paths_rec((0, 0), (dim-1, dim-1), [(0, 0)]))
