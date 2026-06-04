from HelperFunctions import *
from Question2 import GetShortestPath

def GetShortestPathGrid(grid, source, destination):
    G = {} #Initialize a dictionary G to store the graph
    no_of_rows, no_of_cols = len(grid), len(grid[0]) 
    nodes_lst, edges_lst=[], []

    #Enumerate through the grid and add the nodes to G
    for i in range(no_of_rows):
        for j in range(no_of_cols):
            if grid[i][j] != -1: #Checking for obstacle
                nodes_lst.append((i, j))
    G = AddNodes(G, nodes_lst)

    #Enumerate through the grid and add the edge to the list
    for i in range(no_of_rows):
        for j in range(no_of_cols):
            if grid[i][j] != -1: #Checking for obstacle
                #List of potential neighbors (up, down, left, right)
                potential_neighbours = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
                for n_i, n_j in potential_neighbours:
                    #Checking neighbor bounds and obstacle presence
                    if 0 <= n_i < no_of_rows and 0 <= n_j < no_of_cols and grid[n_i][n_j] != -1:
                        edges_lst.append(((i, j), (n_i, n_j), 1))

    #Add edges_lst to the graph G
    G = AddEdges(G, edges_lst, directed=False)
    #At this point our graph is created
    #     
    #GetShortestPath(graph, source, destination)
    return GetShortestPath(G, source, destination)

if __name__ == "__main__":
    grid =[[1, 1, 1], [-1, 1, 1], [1, -1, 1]]
    source = (0, 0)
    destination = (2,2)
    print(GetShortestPathGrid(grid, source, destination))


        