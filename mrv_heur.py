# Most constrained variable

graph = {
    "a": ["red", "green", "blue"],
    "b": ["red", "green"],
    "c": ["blue"],
    "d": ["red", "green", "blue", "purple"],
    "e": ["orange"],
}

counted = list(map(lambda n: (n, len(graph[n])), graph))
sorteed = sorted(counted, key=lambda el: el[1])

print(sorteed)
