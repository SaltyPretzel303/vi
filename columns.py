import math
from queue import PriorityQueue


EMPTY = "_"
TAKEN = "X"

# value greater than 8
MAX_VALUE = 10

# list of columns
table = [[EMPTY for i in range(0, 8)] for j in range(0, 8)]

# dot = (col, row)
dots = [(3, 0), (3, 1), (3, 2), (3, 3), (7, 4), (6, 5), (2, 6), (3, 7)]
dots = [(0, 0), (1, 1), (2, 2), (3, 3), (2, 4), (1, 5), (0, 6), (4, 7)]
dots = [(3, 0), (2, 1), (3, 2), (3, 3), (7, 4), (6, 5), (2, 6), (1, 7)]
dots = [(3, 0), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (3, 6), (3, 7)]

for dot in dots:
	table[dot[0]][dot[1]] = TAKEN


def print_table(t):
	for i in range(0, 8):
		for col in t:
			print(col[i], end="|")

		print()

# a = (col, row)


def swap(table, dots, a, b):

	# print(f"swap {a} <> {b}")
	# new_t = table.copy()
	new_t = [col.copy() for col in table]

	temp = new_t[a[0]][a[1]]
	new_t[a[0]][a[1]] = new_t[b[0]][b[1]]
	new_t[b[0]][b[1]] = temp

	new_d = dots.copy()
	new_d.remove(a)
	new_d.append(b)

	return (new_t, new_d)


def char_to_num(col):
	return [1 if el == TAKEN else 0 for el in col]


def sum_columns(table):
	return [sum(char_to_num(col)) for col in table]


def find_right(cols, start):
	if start == 7:
		# print("find_right -> max")
		return MAX_VALUE
	else:
		for i in range(start+1, len(cols)):
			if cols[i] == 0:
				# print(f"find_right -> {i-start}")
				return i - start

		return MAX_VALUE


def find_left(cols, start):
	if start == 0:
		# print("find_left -> max")
		return MAX_VALUE
	else:
		for i in range(start-1, -1, -1):
			if cols[i] == 0:
				# print(f"find_left -> {start-i}")
				return start - i
		return MAX_VALUE


def evaluate(table, dots):
	t_sum = 0
	cols = sum_columns(table)
	for dot in dots:
		if cols[dot[0]] > 1:
			left = find_left(cols, dot[0])
			right = find_right(cols, dot[0])
			# print(f"for: {dot} l={left} r={right}")
			t_sum += min(left, right)

	conflict_sum = sum([val if val > 1 else 0 for val in cols])
	conflict_cols = sum([1 if val > 1 else 0 for val in cols])

	if conflict_sum > 0:
		t_sum += 8-math.floor(conflict_sum/conflict_cols)

	return t_sum


def arrange(table, dots):

	# (eval, table, steps)
	# possible_s = [(evaluate(table), table,[])]

	queue = PriorityQueue()
	queue.put((evaluate(table, dots), table, dots, []))

	while queue:
		current = queue.get()

		print()

		print_table(current[1])
		print(sum_columns(current[1]), end="=")
		print(evaluate(current[1], current[2]), end=" ")
		print(len(current[3]))

		print()

		if current[0] == 0:
			print("FOUND IT")
			print_table(current[1])
			print(current[3])
			return current[3]

		cols = sum_columns(current[1])

		# dot_queue = PriorityQueue()
		# for dot in current[2]:
		#     dist = min(find_left(cols, dot[0]), find_right(cols, dot[0]))
		#     dot_queue.put((dist, dot))

		dots = list(map(lambda dot: (
			min(find_left(cols, dot[0]), find_right(cols, dot[0])), dot), current[2]))
		dots.sort()
		print(dots)
		dots = list(map(lambda dot: dot[1], dots))

		for dot in dots:
			# print("Traversing nodes ... ")
			# c = 0
			# while dot_queue:

			# dot = dot_queue.get()
			# dot = dot[1]
			# print("Got one ... ")

			if dot[0] > 0:
				n_state = swap(current[1], current[2], dot, (dot[0]-1, dot[1]))
				eval = evaluate(n_state[0], n_state[1])
				if eval != 0:
					eval += len(current[3])+1

				path = current[3]+[((dot[0], dot[1]), -1)]
				queue.put((eval, n_state[0], n_state[1], path))

			if dot[0] < 7:
				n_state = swap(current[1], current[2], dot, (dot[0]+1, dot[1]))
				eval = evaluate(n_state[0], n_state[1])
				if eval != 0:
					eval += len(current[3])+1

				path = current[3]+[((dot[0], dot[1]), +1)]
				queue.put((eval, n_state[0], n_state[1], path))

		# value = input("continue")


arrange(table, dots)
