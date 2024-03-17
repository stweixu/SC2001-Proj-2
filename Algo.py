import sys
import json
import heapq


def load_graph_matrix(v, e, n=0):
    graph = {}
    with open(f"data{v}_{e}_{n}.json", 'r') as openfile:
        # Reading from json file
        graph = json.load(openfile)
    matrix = [[-1 for _ in range(graph['v'])] for _ in range(graph['v'])]
    for i in range(graph['v']):
        for i2 in graph[str(i)]:
            matrix[i][int(i2)] = graph[str(i)][str(i2)]
    return matrix


def dijkstra_matrix_array(matrix):
    num_vertices = len(matrix)
    dist = [sys.maxsize] * num_vertices
    dist[0] = 0
    explored = [False] * num_vertices

    for _ in range(num_vertices):
        # Find the vertex with the minimum distance from the priority queue (array)
        min_dist = sys.maxsize
        min_vertex = -1
        for v in range(num_vertices):
            if not explored[v] and dist[v] < min_dist:
                min_dist = dist[v]
                min_vertex = v

        # If all remaining vertices are unreachable, break the loop
        if min_vertex == -1:
            break

        explored[min_vertex] = True

        # Update distances to its neighbors
        for neighbor in range(num_vertices):
            if not explored[neighbor] and matrix[min_vertex][neighbor] != -1:
                new_distance = dist[min_vertex] + matrix[min_vertex][neighbor]
                if new_distance < dist[neighbor]:
                    dist[neighbor] = new_distance

    return dist


def load_graph_list(v, e, n=0):
    with open(f"data{v}_{e}_{n}.json", 'r') as openfile:
        # Reading from json file
        return json.load(openfile)


def dijkstra_list_heap(adj_list, source=0):
    queue = []
    heapq.heappush(queue, (0, source))
    dist = [sys.maxsize] * adj_list['v']
    dist[0] = 0

    while queue:
        # Extract the vertex with the minimum distance from the priority queue
        current_distance, current_vertex = heapq.heappop(queue)

        for v in adj_list[str(current_vertex)]:
            weight = adj_list[str(current_vertex)][v]
            # If there is a shorter path to v through u.
            if dist[int(v)] > dist[current_vertex] + weight:
                # Updating distance of v
                dist[int(v)] = dist[current_vertex] + weight
                heapq.heappush(queue, (dist[int(v)], int(v)))

    return dist
