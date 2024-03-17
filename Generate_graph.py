import json
import random
import os


def random_exclude(start, end, exclude, num):
    out = []
    while len(out) != num:
        curr = random.randint(start, end)
        if curr not in exclude:
            out.append(curr)
            exclude.append(curr)
    return out


# v = number of vertices
# e = number of edges per vertex
# n = number of graph to generate
def generate_graph(v, e, n=5):

    #get current file directory to store graph
    root = os.getcwd()
    weight_max = 100
    for graph_index in range(n):
        graph = {"v": v}

        for vertex_index in range(v):
            # connect each v to neighbour v+1 to ensure connected graph
            # weight_max * 2 ensures shortest path is not circular
            graph[vertex_index] = {(vertex_index + 1) % v: random.randint(1, weight_max * 2)}

            # add random edges to v excluding neighbour v+1
            for random_vertex in random_exclude(0, v - 1, [vertex_index, (vertex_index + 1) % v], e - 1):
                graph[vertex_index][random_vertex] = random.randint(1, weight_max)
        with open(f"{root}/data{v}_{e}_{graph_index}.json", "w+") as file:
            json_obj = json.dumps(graph)
            file.write(json_obj)


vertex = [1000, 2000, 3000, 4000, 5000, 10000]
edges = [5, 100, 999]
num = 1
time_matrix = {}
time_list = {}

for i in vertex:
    for i2 in edges:
        generate_graph(i, i2, num)

