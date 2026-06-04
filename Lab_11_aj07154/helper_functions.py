import csv

##############################################################################################
############################# COPY YOUR LAB10 FUNCTIONS HERE #################################
def addNodes(G, nodes):
    for node in nodes:
        if node not in G:
            G[node] = []
    return

def addEdges(G, edges, directed=False):
    for edge in edges:
        u, v, weight = edge
        G[u].append(tuple((v, weight)))
        if not directed:
            G[v].append(tuple((u, weight)))
            continue
    return

def displayGraph(G):
    print(G)

def listOfNodes(G):
    return list(G.keys())

def listOfEdges(G, directed=False):
    edgess_lst = []
    seeen_lst = []
    for u in G:
        for v, weight in G[u]:
            if directed or (v, u) not in seeen_lst:
                edgess_lst.append((u, v, weight))
                seeen_lst.append((u, v))
    return edgess_lst

def getNeighbors(G, node):
    lst=[]
    for v, val in G[node]:
        lst.append(v)
    return lst

def removeNode(G, node):
    del G[node]
    for u in G:
        G[u] = [(v, weight) for v, weight in G[u] if v != node]

def removeNodes(G, nodes):
    for node in nodes:
        removeNode(G, node)

def getNearestNeighbor(G, node):
    neighbors = G[node]
    if not neighbors:
        return None
    min_weight = float('inf')
    nearest_neighbor = None
    for neighbor, weight in neighbors:
        if weight < min_weight:
            min_weight = weight
            nearest_neighbor = neighbor
    return nearest_neighbor


##############################################################################################
############################# COMPLETE YOUR LAB11 FUNCTIONS HERE #############################

def in_out_degree(G):
    in_out_deg = {}
    for node in G:
        out_deg = len(G[node])
        in_deg = sum([1 for k in G if node in [t[0] for t in G[k]]])
        in_out_deg[node] = (in_deg, out_deg)
    return in_out_deg

def degree(G):
    deg = {}
    nodes = listOfNodes(G)
    for node in nodes:
        in_neighbors = getInNeighbors(G, node)
        out_neighbors = getOutNeighbors(G, node)
        deg[node] = len(set(in_neighbors + out_neighbors))
    return deg

def getInNeighbors(G, node):
    in_neighbors = [k for k in G if node in [t[0] for t in G[k]]]
    return in_neighbors

def getOutNeighbors(G, node):
    out_neighbors = [t[0] for t in G[node]]
    return out_neighbors

def isNeighbor(G, node1, node2):
    return node2 in [t[0] for t in G[node1]]

##############################################################################

def initialize_matrix(rows, cols):
    return [[-1 for _ in range(cols)] for _ in range(rows)]

def adjlst_to_adj_matrix(G):
    nodes = list(G.keys())
    node_idx = {node: idx for idx, node in enumerate(nodes)}
    matrix = initialize_matrix(len(nodes), len(nodes))
    for node in G:
        for neighbor, weight in G[node]:
            matrix[node_idx[node]][node_idx[neighbor]] = weight
    return matrix

##############################################################################

import csv

def csv_to_adj_list(filename):
    G = {}
    with open(filename, mode='r') as file:
        reader = csv.reader(file)
        headers = next(reader)[1:]  # Get the header row and skip the first column header
        for row in reader:
            node = row[0]
            G[node] = []
            for neighbor, weight in zip(headers, row[1:]):
                try:
                    weight = int(weight)
                    if weight != -1:
                        G[node].append((neighbor, weight))
                except ValueError:
                    continue
    return G

