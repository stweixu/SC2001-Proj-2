import matplotlib.pyplot as plt
import json

vertex = [1000, 2000, 3000, 4000, 5000, 10000]
edges = [5, 100, 999]
array = None
heap = None
with open(f"matrix_time.json", 'r') as openfile:
    array = json.load(openfile)
with open(f"list_time.json", 'r') as openfile:
    heap = json.load(openfile)

# line 1 points

for i in vertex:
    array_time = []
    heap_time = []
    for i2 in edges:
        array_time.append(array[f"{i}_{i2}"])
        heap_time.append(heap[f"{i}_{i2}"])
    plt.plot(edges, array_time, label="Array_Matrix")
    plt.plot(edges, heap_time, label="Heap_List")
    plt.title(f"Vertex = {i}")
    plt.xlabel('Edges')
    plt.ylabel('Time')
    plt.legend()
    plt.savefig(f'{i}.png')
    plt.show()


