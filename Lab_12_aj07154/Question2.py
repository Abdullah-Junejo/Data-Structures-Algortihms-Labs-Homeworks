from Helper_Functions import *

def check_cycles(G, lst):
    if not lst: #Empty lst check
        return False
    start_node = lst[0]
    current_node = start_node
    
    for next_node in lst[1:]:
        found = False
        for neighbor, weight in G[current_node]:
            if neighbor == next_node:
                current_node = next_node
                found = True
                break
        if not found:
            return False
    
    #Check if the last node has starting node as its outdegree neighbour
    for neighbor, _ in G[current_node]:
        if neighbor == start_node:
            return True
    
    return False

# # Testing
G = {'Dallas': [('Austin', 200), ('Denver', 780), ('Chicago', 900)], 'Austin': [('Dallas', 200), ('Houston', 160)], 'Washington': [('Dallas', 1300), ('Atlanta', 600)], 'Denver': [('Atlanta', 1400), ('Chicago', 1000)], 'Atlanta': [('Washington', 600), ('Houston', 800)], 'Chicago': [('Denver', 1000)], 'Houston': [('Atlanta', 800)]}
print(check_cycles(G, ['Dallas','Denver','Atlanta','Washington']))
# # Should print True