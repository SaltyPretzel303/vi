
from queue import PriorityQueue


graph = {
	"a": ["b", "c"],
	"b": ["d", "e"],
	"c": ["f", "g"],
	"d": ["h"],
	"e": ["i", "g"],
	"f": ["j"],
	"g": ["j"],
	"h": [],
	"i": ["j"],
	"j": []}

costs = {
	"a": 9,
	"b": 6,
	"c": 7,
	"d": 4,
	"e": 8,
	"f": 3,
	"g": 4,
	"h": 4,
	"i": 3,
	"j": 0}

rich_graph = {
	"A": (9, [("B", 4), ("C", 6)]),
	"B": (6, [("D", 4), ("E", 2)]),
	"C": (7, [("G", 4), ("F", 6)]),
	"D": (4, [("H", 4)]),
	"E": (8, [("G", 5), ("I", 5)]),
	"F": (3, [("J", 4)]),
	"G": (4, [("J", 5)]),
	"H": (4, []),
	"I": (3, [("J", 3)]),
	"J": (0, [])
}

def evaluate(graph, costs):
	return {n: {"v": costs[n], "c": graph[n]} for n, c in zip(graph, costs)}

def follow_back(prevs, end):
	path = []

	current = end
	while current != None:
		path.append(current)

		current = prevs[current]

	path.reverse()

	return path


def wide_walk(graph, start, target):
	next_queue = []
	prev = {}

	done = []

	next_queue.append(start)
	prev[start] = None

	found = False

	while len(next_queue) > 0 and not found:
		current = next_queue.pop(0)

		if current == target:
			found = True
			return follow_back(prev, current)

		for child in graph[current]:
			if not child in prev:
				next_queue.append(child)
				prev[child] = current

			if child == target:
				return follow_back(prev, child)

		done.append(current)

		print(next_queue, end="\t\t")
		print(graph[current], end="\t\t")
		print(done, end="\t\t")
		print(prev, end="\t\n")

	return []


def deep_walk(graph, start, target):
	next_stack = [start]
	prev = {start: None}

	done = []

	while len(next_stack) > 0:
		current = next_stack.pop()

		if current == target:
			return follow_back(prev, current)

		for child in reversed(graph[current]):
			if child not in prev:
				next_stack.append(child)
				prev[child] = current

			if child == target:
				return follow_back(prev, child)

		done.append(current)

		print(next_stack, end="\t\t")
		print(graph[current], end="\t\t")
		print(done, end="\t\t")
		print(prev, end="\t\n")


def hill_climb(graph, costs, start, target):
	next_stack = [start]
	prev = {start: None}

	nodes = evaluate(graph, costs)

	while len(next_stack) > 0:
		current = next_stack.pop()
		print(current)

		if current == target:
			return follow_back(prev, current)

		print(nodes[current]["c"])

		children = [(nodes[child]["v"], child)
					for child in nodes[current]["c"]
					if child not in prev]
		children.sort(reverse=True)

		print(children)

		for child in children:
			prev[child[1]] = current
			next_stack.append(child[1])

def a_star(graph, start, target):
	reached = PriorityQueue()
	reached.put((0,start))
	prev = {start:None}
	done = {}

	while len(reached) >0 :
		(curr_cost, curr_node) = reached.get()

		if curr_node == target:
			return follow_back(prev, curr_node)

		

			



# print(wide_walk(graph, "a", "j"))
# print(deep_walk(graph, "a", "j"))
# print(hill_climb(graph, costs, "a", "j"))
print(a_star(rich_graph, "a","j"))
