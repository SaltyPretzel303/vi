from queue import PriorityQueue

# Branch and Bound
# not sure if this alg. is considered first-best

graph = {
    "ns": [("ns", -1), ("bg", 78), ("va", -1), ("kg", -1), ("bo", -1), ("ca", -1), ("ue", -1), ("ni", -1)],
    "bg": [("ns", -1), ("bg", -1), ("va", 75), ("kg", 95), ("bo", -1), ("ca", -1), ("ue", -1), ("ni", -1)],
    "va": [("ns", -1), ("bg", -1), ("va", -1), ("kg", 87), ("bo", -1), ("ca", 56), ("ue", 46), ("ni", -1)],
    "kg": [("ns", -1), ("bg", -1), ("va", -1), ("kg", -1), ("bo", 94), ("ca", 46), ("ue", 87), ("ni", -1)],
    "bo": [("ns", -1), ("bg", -1), ("va", -1), ("kg", -1), ("bo", -1), ("ca", -1), ("ue", -1), ("ni", 84)],
    "ca": [("ns", -1), ("bg", -1), ("va", -1), ("kg", -1), ("bo", -1), ("ca", -1), ("ue", 40), ("ni", -1)],
    "ue": [("ns", -1), ("bg", -1), ("va", -1), ("kg", -1), ("bo", -1), ("ca", -1), ("ue", -1), ("ni", 175)]
}

queue = PriorityQueue()

prev = {}


def back_trace(dest, acc=0):
    if prev[dest] is None:
        return acc

    print(f"in: {dest} with: {prev[dest][0]} from: {prev[dest][1]}")
    return back_trace(prev[dest][1], acc+prev[dest][0])


def filter_branches(arr):
    return list(filter(lambda el: el[1] > 0, arr))


def measure_dist(start, dest) -> int:
    #		  (cost, node)
    queue.put((0, start))
    prev[start] = None

    while not queue.empty():
        current = queue.get()
        print(f"c: {current}")

        c_cost = current[0]
        c_name = current[1]

        if c_name == dest:
            return back_trace(dest)

        for branch in filter_branches(graph[c_name]):
            b_name = branch[0]
            b_cost = branch[1]

            if b_name not in prev or prev[b_name][0] > c_cost + b_cost:
                cost = c_cost + b_cost
                print(
                    f"adding: {b_name} cost: {c_cost}+{b_cost} = {cost} prev: {c_name}")
                prev[b_name] = (cost, c_name)
                queue.put((cost, b_name))

        print()

    return -1


measure_dist('ns', 'ni')
