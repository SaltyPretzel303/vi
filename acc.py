from collections.abc import Sequence as seq

from functools import reduce

from itertools import accumulate
from itertools import islice
from itertools import zip_longest


def acc(x, y):
    print((x, y), end='')
    print(f"={x+y}", end=" ")
    return x+y

# print(list(accumulate(range(1,10),acc,initial=1)))


m_range = range(1, 10)

# print(list(m_range))
# print(list(accumulate(m_range, lambda x, y: x+y, initial=0)))


def ranger(gen, value):
    while True:
        yield value
        value = gen(value)


def generator(duo):
    return (duo[1], duo[0]+duo[1])


def fib():
    return (x for x, _ in ranger(generator, (0, 1)))

# print(list(islice(fib(),0,10)))


def is_arr(par) -> int:
    return isinstance(par, seq)


def counter(arr):
    c = 0
    for item in arr:
        if is_arr(item):
            c += counter(item)
        else:
            c += 1

    return c


# arr = [1,2,[3,4,[5,6],7],8,9,[10,[11,[12]]]]
# arr = [1, [1, 3, [2, 4, 5, [5, 5], 4]], [2, 4], 4, 6]
# print(counter(arr))


def diffs(arr):
    return list(reduce(lambda x, y: x-y, range(1, 100)))


arr = [1, 2, 4, 7, 9]
# print(diffs(arr))


def check(value_1, value_2):
    if value_1 == value_2:
        return True

    return False


def check(duo):
    return duo[0] == duo[1]


def toupler(value_1, value_2):
    if check(value_1, value_2):
        return (value_1, value_2, "jeste")
    else:
        return (value_1, value_2, "nije")


def compare(arr_1, arr_2):
    return list(map(toupler, arr_1, arr_2))

# print(compare([1, 7, 2, 4], [2, 5, 2]))
# print(list(zip_longest([1, 2, 3, 4], [5, 6, 7], fillvalue=0)))


# print([(duo[0], duo[1], "jeste") if check(duo) else (duo[0], duo[1], "nije")
#        for duo in zip_longest([1, 7, 2, 4], [2, 5, 2], fillvalue=0)])

# print([{"prvi": duo[0], "drugi":duo[1]} for duo in zip_longest([1, 7, 2, 4], [2, 5, 2], fillvalue=0)])

sum_seq = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


def sumator(x, y):
    val_x = x
    if is_arr(x):
        val_x = budget_sum(x)

    val_y = y
    if is_arr(y):
        val_y = budget_sum(y)

    return val_x + val_y


def budget_sum(arr):
    return reduce(sumator, arr)


# print(budget_sum(sum_seq))

def tuple_sums(arr):
	return {item[0]:sum(item[1:]) for item in arr}


# print(tuple_sums([(1,2),(2,2,3),(3,2,3,4),(9,)]))

sublists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
shortlist = [1,2,3]

# print(list( map(lambda l1,l2: (reduce(lambda x,y: x+y, l1),l2), sublists, shortlist) ))

# [1, 7, 2, 4, 5], [2, 5, 2]

# print(list( (l1,l2) if l1<l2 else (l2,l1) for l1, l2 in  zip_longest([1, 7, 2, 4, 5], [2, 5, 2], fillvalue = 0)  ))

# print([el if not isinstance(el, seq) else reduce(lambda x,y: x*y, el) for el in [1,[2,3],4]])