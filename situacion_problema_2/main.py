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

if __name__ == '__main__':
    cities_dist, data_cap, station_loc = fetch_info("map1.txt")

    optimal_trip = tsp(cities_dist, 0)



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
