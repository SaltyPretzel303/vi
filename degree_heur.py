# Degree heuristic

graph = {
    'a': ['b', 'c', 'e'],
    'b': ['a', 'e'],
    'c': ['a', 'e'],
    'd': ['e']
}


def degree():
    return sorted([(el, len(graph[el])) for el in graph], key=lambda x: x[1], reverse=True)


def degree_map():
    return sorted(map(lambda node: (node, len(graph[node])), graph), key=lambda el: el[1], reverse=True)


print(degree())

print(" ")

print(degree_map())
