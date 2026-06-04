from Helper_Functions import *

def dfs(G, s):
    stack = Initialize(len(G))
    push(stack, s)
    visited = []
    while not is_empty(stack):
        a = pop(stack)
        if a not in visited:
            visited.append(a)
            for i in G[a]:
                if i[0] not in visited:
                    push(stack, i[0])
    return visited


# # Testing 
G = {0: [(1, 1), (2, 1)], 1: [(2, 1), (3, 1)], 2: [(4, 1)], 3: [(4, 1), (5, 1)], 4: [(5, 1)], 5: []}
print(dfs(G, 0))
# # Should print [0, 2, 4, 5, 1, 3]