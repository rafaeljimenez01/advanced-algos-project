
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
                    neighborhood_distance[node][neighbor] = distance[neighbor]

        file.readline() # skip empty line.

        # TODO: fetch and process data capacity matrix.

        file.readline() # skip empty line.

        # TODO: fetch and process statrion location list.

        return neighborhood_distance, data_cap, station_location


if __name__ == '__main__':
    neighborhoods_dist, data_cap, station_loc = fetch_info("map1.txt")
