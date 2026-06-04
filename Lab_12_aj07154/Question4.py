from Helper_Functions import *

def BFS_Modified(G, root, lvl):
    queue = Initialize(len(G))
    enQueue(queue, (root, 0))  #(node, level)
    visited = []
    levels = {}

    while not is_empty(queue):
        x, level = deQueue(queue)
        if level not in levels:
            levels[level] = []
        levels[level].append(x)
        for neighbor, weight in G[x]:
            if neighbor not in visited:
                enQueue(queue, (neighbor, level + 1))
                visited.append(neighbor)
    return levels.get(lvl, [])

def nodes_of_level(G, level):
    if not G:
        return []
    start_node = list(G.keys())[0]  #Assuming the first key since there is no start node in function argument.
    return sorted(BFS_Modified(G, start_node, level))

# # Testing
G = {'s': [(1, 1), (2, 1)], 1: [(3, 1), (4, 1), (5, 1)], 2: [(6, 1)], 3: [], 4: [], 5: [], 6: [(7, 1)], 7: []}

print(nodes_of_level(G, 3))
# # Should print [7]

print(nodes_of_level(G, 1))
# # Should print [1, 2]

inp = {'Dallas': [('Austin', 200), ('Denver', 780), ('Washington', 1300)], 
       'Austin': [('Houston', 160), ('Chicago', 900)], 
       'Washington': [('Atlanta', 600)], 
       'Denver': [], 
       'Atlanta': [], 
       'Chicago': [], 
       'Houston': [] }

print(nodes_of_level(inp, 2))  #The answer is correct though different order despite using sorted