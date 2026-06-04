from helper_functions import *


def one_way_connection(G):
    one_way = []
    for u in G:
        for v, weight in G[u]:
            if (v in G and (u, weight) not in G[v]):
                one_way.append((u, v))
    return one_way

def nearest_airport(G, A):
    neighbors = G[A]
    if not neighbors:
        return None
    min_distance = float('inf')
    nearest = None
    for neighbor, distance in neighbors:
        if distance < min_distance:
            min_distance = distance
            nearest = neighbor
    return nearest

def get_in_degree_neighbors(G, node):
    """Helper function to get in-degree neighbors of the given destination airport."""
    in_degree_neighbors = set()
    for u in G:
        for v, weight in G[u]:
            if v == node:
                in_degree_neighbors.add(u)
    return in_degree_neighbors

def not_more_than_one_intermediate(G, node):
    first_level_neighbors = get_in_degree_neighbors(G, node)
    all_neighbors = set(first_level_neighbors)

    for neighbor in first_level_neighbors:
        second_level_neighbors = get_in_degree_neighbors(G, neighbor)
        all_neighbors.update(second_level_neighbors)

    all_neighbors.discard(node)  # Remove the original node if it's in the set
    return list(all_neighbors)


def main():
    # Create graph
    G = {}
    nodes = ['Dallas', 'Austin', 'Washington', 'Denver', 'Atlanta', 'Chicago', 'Houston']
    addNodes(G, nodes)
    
    edges = [
        ('Dallas', 'Austin', 200),
        ('Dallas', 'Denver', 780),
        ('Dallas', 'Chicago', 900),
        ('Austin', 'Dallas', 200),
        ('Austin', 'Houston', 160),
        ('Washington', 'Dallas', 1300),
        ('Washington', 'Atlanta', 600),
        ('Denver', 'Atlanta', 1400),
        ('Denver', 'Chicago', 1000),
        ('Atlanta', 'Washington', 600),
        ('Atlanta', 'Houston', 800),
        ('Chicago', 'Denver', 1000),
        ('Houston', 'Atlanta', 800)
    ]

    addEdges(G, edges, directed=True)
    output = ""
    output += "GRAPH\n"
    output += str(G) + "\n"

    output += "\nONE WAY CONNECTION\n"
    one_way = one_way_connection(G)
    output += str(one_way) + "\n"

    output += "\nNEAREST AIRPORT\n"
    for airport in G:
        nearest = nearest_airport(G, airport)
        output += f"{airport} : {nearest}\n"

    output += "\nCONNECTED WITH NOT MORE THAN ONE INTERMEDIATE AIRPORT\n"
    example_node = 'Dallas'
    connected_airports = not_more_than_one_intermediate(G, example_node)
    output += f"{example_node} : {connected_airports}\n"

    # Removing Washington and adding new route
    del G['Washington']
    for u in G:
        G[u] = [(v, weight) for v, weight in G[u] if v != 'Washington']

    addEdges(G, [('Atlanta', 'Dallas', 1700), ('Dallas', 'Atlanta', 1700)], directed=True)

    output += "\nREMOVING WASHINGTON, ADDING PATH FROM ATLANTA TO DALLAS AND DISPLAYING A GRAPH\n"
    output += str(G) + "\n"

    print(output)

if __name__ == "__main__":
    main()


#Original Comment
'''
EXPECTED OUTPUT:

GRAPH
{'Dallas': [('Austin', 200), ('Denver', 780), ('Chicago', 900)], 'Austin': [('Dallas', 200), ('Houston', 160)], 'Washington': [('Dallas', 1300), ('Atlanta', 600)], 'Denver': [('Atlanta', 1400), ('Chicago', 1000)], 'Atlanta': [('Washington', 600), ('Houston', 800)], 'Chicago': [('Denver', 1000)], 'Houston': [('Atlanta', 800)]}

ONE WAY CONNECTION
[('Dallas', 'Denver'), ('Dallas', 'Chicago'), ('Austin', 'Houston'), ('Washington', 'Dallas'), ('Denver', 'Atlanta')]

NEAREST AIRPORT
Dallas : Austin
Austin : Houston
Washington : Atlanta
Denver : Chicago
Atlanta : Washington
Chicago : Denver
Houston : Atlanta

CONNECTED WITH NOT MORE THAN ONE INTERMEDIATE AIRPORT
Dallas : ['Austin', 'Washington', 'Atlanta']

REMOVING WASHINGTON, ADDING PATH FROM ATLANTA TO DALLAS AND DISPLAYING A GRAPH
{'Dallas': [('Austin', 200), ('Denver', 780), ('Chicago', 900), ('Atlanta', 1700)], 'Austin': [('Dallas', 200), ('Houston', 160)], 'Denver': [('Atlanta', 1400), ('Chicago', 1000)], 'Atlanta': [('Houston', 800), ('Dallas', 1700)], 'Chicago': [('Denver', 1000)], 'Houston': [('Atlanta', 800)]}
'''