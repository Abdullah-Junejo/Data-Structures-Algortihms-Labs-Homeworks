import csv
import pandas as pd
from collections import deque, defaultdict




def addVertices(G: dict, vertices: list):
    for vertex in vertices:
        #adding the vertex not present in G into a list
        if vertex not in G:
            G[vertex]=[]

def addEdges(G: dict, edges: list):
    for edge in edges:
        node1, node2, weight= edge
        #adding the nodes along with their weights, which represent the edges
        G[node1].append((node2, weight))
        G[node2].append((node1,weight))

def create_flight_network(filename: str, option: int):
# Read the CSV file into a pandas DataFrame
    df = pd.read_csv(filename)
    
    graph = defaultdict(list)  # Using defaultdict to automatically handle missing keys
    
    for _, row in df.iterrows():
        origin = row['Origin City'].strip()
        destination = row['Destination City'].strip()
        weight = row['Duration'] if option == 1 else row['Distance']
        
        # Add the edge to the graph
        graph[origin].append((destination, weight))
        
        # Optionally, add the reverse edge if an undirected graph is needed
        # graph[destination].append((origin, weight))
    
    # Convert defaultdict to a regular dict for better readability in output
    return dict(graph)


def get_flight_connections(graph: dict, city: str, option: str) -> list:
    if option == 'o':
        # Outbound flights from the city
        return [destination for destination, _ in graph.get(city, [])]
    elif option == 'i':
        # Inbound flights to the city
        inbound_connections = []
        for origin, destinations in graph.items():
            if origin != city:
                for destination, _ in destinations:
                    if destination == city:
                        inbound_connections.append(origin)
        return inbound_connections
    else:
        raise ValueError("Option must be 'i' for inbound flights or 'o' for outbound flights.")


def get_number_of_flight_connections(graph: dict, 
                                     city: str, 
                                     option: str) -> int:
    connections = get_flight_connections(graph, city, option)
    return len(connections)

def get_flight_details(graph: dict, origin: str, destination: str) -> int:
    # Check if the origin city is in the graph
    if origin not in graph:
        return None
    
    # Search for the destination city in the outbound flights from the origin city
    for dest, weight in graph[origin]:
        if dest == destination:
            return weight
    
    # If destination city is not connected to the origin city
    return -1

def add_flight(graph: dict, origin: str, destination: str, weight: int):
     # Check if both origin and destination cities exist in the graph
    if origin not in graph:
        print(f"City '{origin}' not present in the flight network.")
        return
    if destination not in graph:
        print(f"City '{destination}' not present in the flight network.")
        return
    
    # Check if the connection already exists and update it
    for i, (dest, _) in enumerate(graph[origin]):
        if dest == destination:
            graph[origin][i] = (destination, weight)
            print(f"Updated flight from {origin} to {destination} with weight {weight}.")
            return
    
    # If the connection does not exist, add it
    graph[origin].append((destination, weight))
    print(f"Added flight from {origin} to {destination} with weight {weight}.")



def add_airport(graph: dict, city: str, destination: str, weight: int):
    # Check if the new city already exists in the graph
    if city in graph:
        print(f"Airport '{city}' already exists in the flight network.")
        return
    
    # Check if the destination city exists in the graph
    if destination not in graph:
        print(f"Destination city '{destination}' not present in the flight network.")
        return
    
    # Add the new city to the graph with a connection to the destination city
    graph[city] = [(destination, weight)]
    print(f"Added new airport '{city}' with a flight to '{destination}' with weight {weight}.")
    
    # Optionally, also add the reverse connection if needed
    # Uncomment the following lines if reverse connections are desired
    # graph[destination].append((city, weight))
    # print(f"Added reverse flight from '{destination}' to '{city}' with weight {weight}.")


def get_secondary_flights(graph: dict, city: str):
    print(graph)
    if city not in graph:
        return None
    
    # Get immediate connections from the city
    immediate_connections = [destination for destination, _ in graph[city]]
    print(immediate_connections)
    # Collect all unique secondary cities
    
    secondary_cities=[]
    
    for connection in immediate_connections:
        for dest,_ in graph[connection]:
            if dest not in secondary_cities:
                secondary_cities.append(dest)
        
       
    
    # Return the sorted list of unique secondary cities
    return secondary_cities


def counting_common_airports(graph: dict, cityA: str, cityB: str) -> int:
    # Check if both cities exist in the graph
    if cityA not in graph or cityB not in graph:
        return 0
    
    # Retrieve outbound connections for both cities
    outbound_A = set(destination for destination, _ in graph[cityA])
    outbound_B = set(destination for destination, _ in graph[cityB])
    
    # Find common airports
    common_airports = outbound_A.intersection(outbound_B)
    
    # Return the count of common airports
    return len(common_airports)


def remove_flight(graph: dict, origin: str, destination: str):
    # Check if the origin city is in the graph
    if origin not in graph:
        print(f"City '{origin}' not present in the flight network.")
        return
    
    # Check if the destination city is in the graph
    if destination not in graph:
        print(f"City '{destination}' not present in the flight network.")
        return
    
    # Remove the connection from origin to destination
    graph[origin] = [conn for conn in graph[origin] if conn[0] != destination]
    
    # Remove the connection from destination to origin (if bidirectional)
    graph[destination] = [conn for conn in graph[destination] if conn[0] != origin]
    
    print(f"Removed flight from {origin} to {destination}.")

def remove_airport(graph: dict, city: str):
    # Check if the city exists in the graph
    if city not in graph:
        print(f"City '{city}' not present in the flight network.")
        return
    
    # Remove the city and all its connections
    del graph[city]
    
    # Remove all connections to the city from other cities
    for other_city in graph:
        graph[other_city] = [conn for conn in graph[other_city] if conn[0] != city]
    
    print(f"Removed city '{city}' and all its connections.")


def DFS_all_routes(graph: dict,
                    origin: str, 
                    destination: str,
                    route: list, 
                    all_routes: list):
    # Append the origin city to the current route
    route.append(origin)

    # If the origin city is the same as the destination city, add the current route to all_routes
    if origin == destination:
        all_routes.append(route[:])  # Append a copy of the route to all_routes
    else:
        # Explore neighbors of the origin city
        for neighbor in graph[origin]:
            # If the neighbor is not already visited (not in the current route), explore it
            if neighbor not in route:
                # Recursively call DFS_all_routes with the neighbor as the new origin
                DFS_all_routes(graph, neighbor, destination, route[:], all_routes)

def find_all_routes(graph: dict, origin: str, destination: str):
     # Helper function for DFS
    def dfs(current, path):
        if current == destination:
            all_paths.append(path.copy())
            return
        
        if current not in graph:
            return
        
        for neighbor, _ in graph[current]:
            if neighbor not in path:  # Avoid cycles
                path.append(neighbor)
                dfs(neighbor, path)
                path.pop()  # Backtrack
    
    # Check if both origin and destination exist in the graph
    if origin not in graph or destination not in graph:
        return None
    
    # If origin is the same as destination, return an empty list
    if origin == destination:
        return []
    
    all_paths = []
    dfs(origin, [origin])
    
    return all_paths

def DFS_layovers(graph: dict, origin: str, destination: str, 
                 route: list, 
                 layovers_lst: list):
     # Append the current city to the current route
    route.append(origin)

    # If the origin city is the same as the destination city, calculate layovers
    if origin == destination:
        layovers = len(route) - 2  # Subtract 2 to exclude origin and destination
        layovers_lst.append(layovers)
    else:
        # Explore neighbors of the origin city
        for neighbor, _ in graph.get(origin, []):
            if neighbor not in route:  # Avoid revisiting cities in the current route
                DFS_layovers(graph, neighbor, destination, route[:], layovers_lst)

def find_number_of_layovers(graph: dict, origin: str, destination: str):
        # Edge cases: Check if origin or destination is missing or if they are the same
    if origin not in graph or destination not in graph:
        return None
    if origin == destination:
        return []

    # Initialize list to store the number of layovers for all routes
    layovers_list = []

    # Perform DFS to find layovers for all possible routes
    DFS_layovers(graph, origin, destination, [], layovers_list)

    # Return the sorted list of layovers
    return sorted(layovers_list)

