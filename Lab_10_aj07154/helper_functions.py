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
