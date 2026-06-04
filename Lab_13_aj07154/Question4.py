from HelperFunctions import *
from Question2 import GetShortestPath

def GetShortestDistanceBetweenCities(source, destination):
    # Write your code here
    #Read the CSV file ’connections.csv’.
    file_path = 'connections.csv' 
    with open(file_path, mode='r') as file:
        csv_reader = csv.reader(file)
        connections = list(csv_reader) #Convert the CSV data into a list.
    city_names_lst = connections[0][1:]

    G = {} #Initialize empty dictionary for the adjacency list..
    G = AddNodes(G, city_names_lst)

    #Create an adjacency list representation of the graph using the CSV data
    edges_lst = []
    for i in range(1, len(connections)):
        for j in range(1, len(connections[i])):
            if connections[i][j] != '-1': 
                starting_city = connections[i][0]
                ending_city = connections[0][j]
                distance = int(connections[i][j])
                edges_lst.append((starting_city, ending_city, distance))

    G = AddEdges(G, edges_lst, directed=False)

    #GetShortestPath(graph,source,destination).
    return GetShortestPath(G, source, destination)

if __name__ == "__main__":
    print(GetShortestDistanceBetweenCities("Islamabad",'Nathiagali'))

    