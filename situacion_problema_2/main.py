import sys
import copy
from collections import defaultdict

def build_matrix(size, file):
    matrix = []

    file.readline() # Skip empty line.

    # Fetch and process distance matrix.
    for node in range(size):
        distance = file.readline().rsplit()
        matrix.append([])

        # Add neighbors to node list. 
        for neighbor in range(size):
            matrix[node].append(int(distance[neighbor]))

    return matrix

# INPUT: file_name -> string.
# OUTPUT: main_string -> string(file content)
# Description: Returns the file content.
def fetch_info(file_name):
    # Open file to extract info.
    with open(file_name) as file:
        size = int(file.readline().rsplit()[0])
        neighborhood_distance = build_matrix(size, file)
        data_cap = build_matrix(size, file)
        station_location = []

        # TODO: fetch and process statrion location list.

        return neighborhood_distance, data_cap, station_location

# Traveling salesman probelm using lexicographic order.
def tsp(distances, origin):
    # store all c apart from source vertex
    cities = []
    path = []

    for city in range(len(distances[0])):
        if city != origin:
            cities.append(city)

    # store minimum weight Hamiltonian Cycle
    min_path = sys.maxsize
    possible_paths = get_lexographic_order(cities)
    for current_path in possible_paths:

        # store current Path weight(cost)
        current_distance = 0

        # compute current path weight
        current_city = origin
        for next_city in current_path:
            current_distance += distances[current_city][next_city]
            current_city = next_city

        current_distance += distances[current_city][origin]

        # update minimum
        min_path = min(min_path, current_distance)
        if min_path == current_distance:
            path = current_path

    return min_path, path

def get_lexographic_order(lst):
    lex_set = [lst]

    while True:
        largest_x, largest_y = -1, -1

        # Find largest x such that P[x] < P[x+1].
        for i in range(len(lst) - 1):
            if lst[i] < lst[i + 1]:
                largest_x = i;

        # When there is no value that satisfies largest_x there are no more permutations.
        if largest_x == -1:
            break

        # Find largest y such that P[x] < P[y].
        for j in range(len(lst)):
            if lst[largest_x] < lst[j]:
                largest_y = j

        # Swap P[x] and P[y].
        tmp = copy.copy(lst)
        tmp[largest_x], tmp[largest_y] = tmp[largest_y], tmp[largest_x]

        # reverse P[x +1 ... n] and add it to lexographical order set.
        lst = tmp[:largest_x + 1:] + tmp[-1:largest_x:-1]
        lex_set.append(lst)

    return lex_set



####################

#Floyd-Warshall algorithm -Based on GfG https://www.geeksforgeeks.org/floyd-warshall-algorithm-dp-16/
#Finds the sortest paths in a directed and weightyed graph
#Input: Graph (adjency matrix)
#Output: 2x2 matrix with the shortest paths(similar to adjency matrix but with shortest paths)
#Time complexity: O(V^3) where V is the number of vertices the graph has

####################

def floyd(graph):

    # This will initialize the result matrix, and will contain the
    # sortest distances between every pair of vertices
    V = len(graph)
    solution = graph


    #We will take every possible vertex as an intermediate vertex, named K
    for k in range(V):

        # We will take i as the soruce vertex (from where the path would begin)
        for i in range(V):

            # We will take j as the vertex of destination for every i(source)
            for j in range(V):

                # We can make two decisions, to take the k intermidiate vertex 
                # of to skip it. We will take it into account only if the k vertex
                # is part of the shortest path

                if solution[i][k] + solution[k][j] < solution[i][j]:
                    solution[i][j] = solution[i][k] + solution[k][j]


    return solution


#####################

#Ford-Fulkerson algorithm -Based on GfG https://www.geeksforgeeks.org/ford-fulkerson-algorithm-for-maximum-flow-problem/
#Given a weighted graph finds that represents the flow in a network where every edge has a capacity.
# This problem was solved using Edmond Karp algorithm which is an extension of the ford-fulkerson algorithm that
#uses BFS for finding the augmented paths
#Finds the maximum flow in from a source to sink
#Input: Graph, source, sink
#Output: Maximum flow of information
#Time complexity: O(EV^3) where V is the number of vertices the graph has and E are the edges

####################

#Bread First Search for finding all the augmented paths

def BFS(rows, graph, source, sink, parent):

    #Set all vertices to not visited
    visited = [False] * rows
    queue = []

    queue.append(source) #Source node visited and added to the queue
    visited[source] = True

    #Start the BFS
    while queue:
        u = queue.pop(0)

        for index, value in enumerate(graph[u]):
            if not visited[index] and value > 0:
                queue.append(index)
                visited[index] = True
                parent[index] = u

    return True if visited[sink] else False

# Applying Ford Fulkerson algorithm
def ford_fulkerson(graph, source, sink):
    flow_max = 0
    parent = [0] * len(graph)

    while BFS(len(graph), graph, source, sink, parent):

        path_flow = float("Inf")
        s = sink
        while s != source:
            path_flow = min(path_flow, graph[parent[s]][s])
            s = parent[s]

        # Adding the path flows
        flow_max += path_flow

        # Updating the residual values of edges
        v = sink
        while v != source:
            u = parent[v]
            graph[u][v] -= path_flow
            graph[v][u] += path_flow
            v = parent[v]

    return flow_max


if __name__ == '__main__':
    cities_dist, flow_graph, station_loc = fetch_info("map1.txt")

    optimal_trip = tsp(cities_dist, 0)

    #adcency_floyd contains the adjancy matrix that it's the result of floyd-warshall algorithm
    adcency_floyd = floyd(cities_dist)
    #display floyd in a nice and easy to understand format

    for i in range(len(adcency_floyd)):
        for j in range(i+1, len(adcency_floyd[0])):
            print("ARCO " + str(i) + " " + str(j) + " costara : " + str(adcency_floyd[i][j]))


    print("Max Flow: %d " % ford_fulkerson(flow_graph, 0, len(flow_graph) - 1))




# def get_route(prev, i, route):
#     if i >= 0:
#         get_route(prev, prev[i], route)
#         route.append(i)

# def dijksra(graph, origin):
#     # Dictionary that stores another dictionary to map a node with all other
#     # neighbors, the shortest distance to travel to each other and the path taken.
#     # (e.g {node: {neighbor_1: {dist, [path]], neighbor_2: {dist, [path]}...}})
#     optimal = {node: {"dist": float('inf'), "path": []} for node in graph}
#     # tuple's list that holds the nodes to be vistied. Each tuple holds the 
#     # distance to the node from the origin and the node to be visited. The order
#     # in which the nodes will be visited depend on the distance value.
#     priority_queue = [(0, origin)]
#     parent = [-1] * len(graph.keys())

#     # Distance from  oirign to itlsef set to 0.
#     optimal[origin]["dist"] = 0

#     # Iterate through priority queue until empty.
#     while priority_queue:
#         # Pop node with smallest distance.
#         current_distance, current_node = heapq.heappop(priority_queue)

#         # Only analize node if the distance to current node is not grater.  
#         if current_distance <= optimal[current_node]["dist"]:

#             for neighbor, traveled_distance in graph[current_node].items():
#                 distance = current_distance + traveled_distance

#                 # Only consider current path if it's better than any path analyzed
#                 # befoire
#                 if distance < optimal[neighbor]["dist"]:
#                     optimal[neighbor]["dist"] = distance 
#                     parent[neighbor] = current_node
#                     heapq.heappush(priority_queue, (distance, neighbor))

#     # adds shortest path to each node.
#     for node in range(len(graph.keys())):
#         if node != origin and optimal[node]["dist"] != sys.maxsize:
#             route = []
#             get_route(parent, node, route)
#             optimal[node]["path"] = route

#     return optimal
