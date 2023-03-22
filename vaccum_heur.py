space = {
    (0, 0): 1, (0, 1): 1,
    (1, 0): 1, (1, 1): 0
}

start = (1, 0)


def is_all_done(space):
    for cell in space:
        if space[cell] == 1:
            print(f"{cell} is dirty")
            return False

    return True


def vacuum(cell, space):
    print("vacuum")
    space[cell] = 0
    return cell


def go_right(cell):
    if cell[1] < 1:
        print(f"right to: {(cell[0], cell[1]+1)}")
        return (cell[0], cell[1]+1)
    else:
        print("no-right")
        return cell


def go_left(cell):
    if cell[1] > 0:
        print(f"left to: {(cell[0], cell[1]-1)}")
        return (cell[0], cell[1]-1)
    else:
        print("no-left")
        return cell


def go_up(cell):
    if cell[0] > 0:
        print(f"up to: {(cell[0]-1, cell[1])}")
        return (cell[0]-1, cell[1])
    else:
        print("no-up")
        return cell


def go_down(cell):
    if cell[0] < 1:
        print(f"down to: {(cell[0]+1, cell[1])}")
        return (cell[0]+1, cell[1])
    else:
        print("no-down")
        return cell


def get_next():
    return [go_right, go_left, go_up, go_down]


def is_dirty(cell, space):
    return space[cell] == 1


def clean(start, space, path=[]):
    print(path)
    if is_dirty(start, space):
        vacuum(start, space)

    if is_all_done(space):
        print("\t DONE")
        return True

    for move in get_next():
        next_cell = move(start)

        if next_cell not in path:
            print("MOVE^")
            is_clean = clean(next_cell, space, path + [next_cell])

            if is_clean:
                return True

    return False


clean(start, space, [start])
