from Helper_Functions import *

def bfs(G,root):
    queue = Initialize(len(G))
    enQueue(queue, root)
    visited = []
    visited.append(root)
    while not is_empty(queue):
        x = deQueue(queue)
        for i in G[x]:
            if i[0] not in visited:
                enQueue(queue, i[0])
                visited.append(i[0])
    return visited

# # Testing
# G = {'s': [(1, 1), (2, 1)], 1: [(3, 1), (4, 1), (5, 1)], 2: [(6, 1)], 3: [], 4: [], 5: [], 6: [(7, 1)], 7: []}
# print(bfs(G,'s'))
# # Should print ['s', 1, 2, 3, 4, 5, 6, 7]