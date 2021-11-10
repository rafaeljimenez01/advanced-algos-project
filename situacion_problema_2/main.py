import sys

def build_matrix(size, file):
    matrix = []

    file.readline() # Skip empty line.

    # Fetch and process distacne matrix.
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

def tsp(distances, origin):
    pass

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
    print("solution")                            

    return solution

if __name__ == '__main__':
    cities_dist, data_cap, station_loc = fetch_info("map1.txt")
    
    optimal_trip = tsp(cities_dist, 0)

    print(floyd(cities_dist))
    



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
