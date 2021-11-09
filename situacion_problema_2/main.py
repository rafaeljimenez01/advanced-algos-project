import heapq
from typing import Optional

def dijksra(graph, origin):
    # Dictionary that stores another dictionary to map a node with all other
    # neighbors and the shortest distance to travel to each other.
    # (e.g {node: {neighbor_1: dist, neighbor_2: dist, ...}})
    distances = {node: float('inf') for node in graph}
    # tuple's list that holds the nodes to be vistied. Each tuple holds the 
    # distance to the node from the origin and the node to be visited. The order
    # in which the nodes will be visited depend on the distance value.
    priority_queue = [(0, origin)]
    
    # Distance from  oirign to itlsef set to 0.
    distances[origin] = 0

    # Iterate through priority queue until empty.
    while priority_queue:
        # Pop node with smallest distance.
        current_distance, current_node = heapq.heappop(priority_queue)

        # Only analize node if the distance to current node is not grater.  
        if current_distance <= distances[current_node]:

            for neighbor, traveled_distance in graph[current_node].items():
                distance = current_distance + traveled_distance

                # Only consider current path if it's better than any path analyzed
                # befoire
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))

    return distances, path


# INPUT: file_name -> string.
# OUTPUT: main_string -> string(file content)
# Description: Returns the file content.
def fetch_info(file_name):
    # Open file to extract info.
    with open(file_name) as file:
        size = int(file.readline().rsplit()[0])
        neighborhood_distance = {}
        data_cap = []
        station_location = []

        file.readline() # Skip empty line.

        # Fetch and process distacne matrix.
        for node in range(size):
            neighborhood_distance[node] = {}
            distance = file.readline().rsplit()

            # Add neighbors to node dict    
            for neighbor in range(len(distance)):
                # Only add nodes that are reachable or not the same node
                if distance[neighbor] != '0':
                    neighborhood_distance[node][neighbor] = int(distance[neighbor])

        file.readline() # skip empty line.

        # TODO: fetch and process data capacity matrix.

        file.readline() # skip empty line.

        # TODO: fetch and process statrion location list.

        return neighborhood_distance, data_cap, station_location


if __name__ == '__main__':
    neighborhoods_dist, data_cap, station_loc = fetch_info("map1.txt")

    neighborhoods_optimal_dist, optimal_path = dijksra(neighborhoods_dist, 0)
    a = 1