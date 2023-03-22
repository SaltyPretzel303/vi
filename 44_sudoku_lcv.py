from functools import reduce

possible = [1, 2, 3, 4]

# Least Constraining Value Heuristic


class mat_pos:
    def __init__(self, r, c):
        self.r = r
        self.c = c


mat = {
    (0, 0): [1, 2, 3, 4],
    (0, 1): [1],
    (0, 2): [1],
    (0, 3): [1],
    #
    (1, 0): [2],
    (1, 1): [1, 2, 3, 4],
    (1, 2): [1, 2, 3, 4],
    (1, 3): [1, 2, 3, 4],
    #
    (2, 0): [1, 2, 3, 4],
    (2, 1): [1, 2, 3, 4],
    (2, 2): [1, 2, 3, 4],
    (2, 3): [1, 2, 3, 4],
    #
    (3, 0): [1, 2, 3, 4],
    (3, 1): [1, 2, 3, 4],
    (3, 2): [1, 2, 3, 4],
    (3, 3): [1, 2, 3, 4]
}


def inters(pos: mat_pos, t_pos):
    same_col_or_r = (pos.r == t_pos[0] or pos.c == t_pos[1])
    same_el = (pos.r == t_pos[0] and pos.c == t_pos[1])

    return same_col_or_r and not same_el


def filter_inter(pos: mat_pos):
    return list(filter(lambda x: inters(pos, x), mat))


def as_possibles(cells):
    return list(map(lambda cell: mat[cell], cells))


def filter_contain(possibles, val):
    return list(filter(lambda pos: val in pos, possibles))


def smart_sum(ells):
    return reduce(lambda x, y: x + (1 if len(y) > 1 else 10), ells, 0)


def lcv(pos: mat_pos):
    return sorted([(val, smart_sum(filter_contain(as_possibles(filter_inter(pos)), val))) for val in mat[(pos.r, pos.c)]], key=lambda el: el[1])


def lcv_map(pos: mat_pos):
    return sorted(list(map(lambda val: (val, smart_sum(filter_contain(as_possibles(filter_inter(pos)), val))), mat[(pos.r, pos.c)])), key=lambda el: el[1])


res = lcv(mat_pos(0, 0))

for el in res:
    print(f"{el[0]} -> {el[1]}")


print("")

res = lcv_map(mat_pos(0, 0))

for el in res:
    print(f"{el[0]} -> {el[1]}")
