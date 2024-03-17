from Generate_graph import *
from Algo import *
from time import process_time
import pandas as pd
import numpy as np


vertex = [1000]
edges = [5, 100, 999]
num = 1
time_matrix = []
time_list = []

for i in vertex:
    for i2 in edges:
        generate_graph(i, i2, num)
        matrix_time = 0
        adj_list_time = 0
        for i3 in range(num):
            matrix = load_graph_matrix(i, i2, i3)
            adj_list = load_graph_list(i, i2, i3)

            start = process_time()
            dijkstra_matrix_array(matrix)
            stop = process_time()
            matrix_time += stop - start

            start = process_time()
            dijkstra_list_heap(adj_list)
            stop = process_time()
            adj_list_time += stop - start
        print(f"Matrix time: {matrix_time/num}")
        print(f"Adj time: {adj_list_time/num}")
        time_matrix.append(matrix_time/num)
        time_list.append(adj_list_time/num)

result = [time_matrix, time_list]
print(result)

result = pd.DataFrame(result)
pd.DataFrame.transpose(result).to_csv("Result.csv", index = True, header=vertex)

# with open(f"matrix_time.csv", "w") as file:
#     json.dump(time_matrix, file)
# with open(f"list_time.csv", "w") as file:
#     json.dump(time_list, file)
