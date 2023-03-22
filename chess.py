from itertools import repeat
import math

table = [[0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 1, 0, 0],
         [0, 0, 1, 0, 0, 0, 0, 0],
         [1, 0, 0, 0, 0, 0, 1, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 1, 0, 0, 0, 0, 0],
         [0, 0, 0, 1, 0, 1, 0, 0],
         [0, 1, 0, 0, 0, 0, 0, 0]]

table = list(
    map(lambda r: list(map(lambda el: "_" if el == 0 else "X", r)), table))


def print_table(table):

    print(" ", end="  ")
    for i in range(0, 8):
        print(i, end=" ")

    print("\n   ", end="")
    for i in range(0, 8):
        print("--", end="")

    print()

    r_c = 0
    for row in table:
        print(r_c, end="| ")
        for el in row:
            print(el, end=" ")

        r_c += 1
        print()


table[7][7] = "F"

print_table(table)


def f_eval(pos, start):
    return pos[0] + math.fabs((pos[1] - start[1]))


def get_next(t, r, c):
    next = [(r-2, c-1), (r-2, c+1),  # up left/right
            (r+2, c-1), (r+2, c+1),  # down left/right
            (r+1, c+2), (r-1, c+2),  # right down/up
            (r+1, c-2), (r-1, c-2)]  # left down/up

    return list(filter(lambda p:
                       p[0] < 8 and
                       p[0] >= 0 and
                       p[1] < 8 and
                       p[1] >= 0 and
                       t[p[0]][p[1]] != "X" and
                       t[p[0]][p[1]] != "F", next))


def follow_back(t, prev, end):
    current = end
    ind = 1
    while current is not None:
        t[current[0]][current[1]] = ind
        ind += 1
        current = prev[current]


def pick_best(set, g, start):
    best = set[0]
    for node in set:
        if g[node] + f_eval(node, start) < g[best] + f_eval(best, start):
            best = node

    return best


def search(t, start):
    done = []
    next_set = [start]
    g = {start: 0}
    prev = {start: None}

    while len(next_set) > 0:
        current = pick_best(next_set, g, start)
        next_set.remove(current)
        t[current[0]][current[1]] = "*"

        print(f"b: {current}")

        if current[0] == 0:
            print("FOUND")
            return follow_back(t, prev, current)

        children = get_next(t, current[0], current[1])

        for child in children:
            if child not in done and child not in next_set:
                next_set.append(child)
                g[child] = g[current] + 3
                prev[child] = current
            else:
                if g[current] + 3 < g[child] + 3:
                    g[child] = g[current] + 3
                    prev[child] = current

                    if child in done:
                        done.remove(child)
                        next_set.append(child)

        print(
            f"{current} -> {list([(child, g[child] + f_eval(child,start)) for child in next_set])}")
        print()
        done.append(current)

    return follow_back(t, prev, (0, 0))


search(table, (7, 7))

print_table(table)
