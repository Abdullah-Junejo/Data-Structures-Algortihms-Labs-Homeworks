from HelperFunctions import *
from Question1 import *

def GetShortestPath(graph, source, destination):
    if source == destination: #Base 
        return -1  
    
    #Initializing as per psuedocode
    output, priority_queue = [],[]
    dist, prev = {},{}

    #For each node v in graph
    for v in graph: #DO
        prev[v] = None
        if v == source: #Then
            dist[v] = 0
            EnQueue(priority_queue, v, 0)
        else:
            dist[v] = float('inf')
            EnQueue(priority_queue, v, float('inf'))
        #ENDIF
    #ENDFOR

    while not IsEmpty(priority_queue): #DO
        v = DeQueue(priority_queue) #Find node v with minimum distance in queue
        #If we reached the destination, break
        if v == destination:
            break

        #Process neighbors of v
        for neighbor, weight in graph[v]:
            alt = dist[v] + weight
            if alt < dist[neighbor]:
                dist[neighbor] = alt
                prev[neighbor] = v
                # Update the priority queue
                EnQueue(priority_queue, neighbor, alt)
    #ENDWHILE 

    #Reconstruct the shortest path if exists
    x = destination
    if dist[x] == float('inf'):
        return -1
    while x is not None:
        output.insert(0, x)
        x = prev[x]
    
    path = []
    if len(output) > 1:
        for i in range(len(output) - 1):
            for neighbor, weight in graph[output[i]]:
                if neighbor == output[i + 1]:
                    path.append((output[i], neighbor, weight))
                    break
    #Return reversed output list if path found, otherwise return −1
    if path:
        return path 
    else:
        return -1

if __name__ == "__main__":
    graph = {'A': [('D', 2), ('E', 6), ('B', 7)], 'B': [('C', 3), ('A', 7)], 'C': [('B', 3), ('D', 2), ('G', 2)], 'D': [('A', 2), ('C', 2), ('F', 8)], 'E': [('A', 6), ('F', 9)], 'F': [('D', 8), ('E', 9), ('G', 4)], 'G': [('C', 2), ('F', 4)]}
    print(GetShortestPath(graph, 'A', 'G'))
    
    



