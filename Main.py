from Generate_graph import *
from Algo import *
from time import process_time
import pandas as pd


def output(v, e, result, filename):
    result_df = pd.DataFrame(result)
    result_df.index = pd.Index(v)
    print("\n output:")
    print(result)
    result_df.to_csv(f"{filename}.csv", index_label="Size", header=e)


vertex = [1000, 2000, 3000, 4000, 5000, 10000]
edges = [5, 100, 999]
num = 1
completed_matrix = []
completed_list = []

for i in vertex:

    temp_matrix = []  # Store adjMatrix result of 1 graph into a temporary list
    temp_list = []  # Store adjList result of 1 graph into a temporary list

    for i2 in edges:
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

        # ENDFOR
        print(f"Matrix time: {matrix_time / num}")
        print(f"Adj time: {adj_list_time / num}")
        temp_matrix.append(matrix_time / num)
        temp_list.append(adj_list_time / num)
        print(f"Temp Matrix: {temp_matrix}")
        print(f"Temp List: {temp_list}")

    # ENDFOR
    completed_matrix.append(temp_matrix)
    completed_list.append(temp_list)

output(vertex, edges, completed_list, "adj_list")
output(vertex, edges, completed_matrix, "adj_matrix")

# matrix_result = pd.DataFrame(time_matrix)
# edges = pd.Index(edges)
# matrix_result = matrix_result.set_index(edges)
# print(matrix_result)
# pd.DataFrame(matrix_result).to_csv("Matrix_Result.csv", index_label="Edges", header=vertex)

# with open(f"matrix_time.csv", "w") as file:
#     json.dump(time_matrix, file)
# with open(f"list_time.csv", "w") as file:
#     json.dump(time_list, file)
