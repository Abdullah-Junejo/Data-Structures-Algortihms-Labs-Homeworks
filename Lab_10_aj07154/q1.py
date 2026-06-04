from helper_functions import *

def main():
    G = {}
    nodes = [1, 2, 3, 4, 5]
    addNodes(G, nodes)
    edges = [(1, 2, 1), (1, 5, 1), (2, 3, 1), (2, 4, 1), (2, 5, 1), (3, 4, 1), (4, 5, 1)]
    addEdges(G, edges, directed=False)

    output = ""
    output += "GRAPH\n"
    output += str(G) + "\n"
    output += "LIST OF NODES\n"
    output += str(listOfNodes(G)) + "\n"
    output += "LIST OF EDGES\n"
    output += str(listOfEdges(G, False)) + "\n"
    output += "NEIGHBOURS FOR EACH NODE IN A GRAPH\n"
    for node in G:
        output += str(node) + " : " + str(getNeighbors(G, node)) + "\n"

    # Expected output
    expected_output = """GRAPH
{1: [(2, 1), (5, 1)], 2: [(1, 1), (3, 1), (4, 1), (5, 1)], 3: [(2, 1), (4, 1)], 4: [(2, 1), (3, 1), (5, 1)], 5: [(1, 1), (2, 1), (4, 1)]}
LIST OF NODES
[1, 2, 3, 4, 5]
LIST OF EDGES
[(1, 2, 1), (1, 5, 1), (2, 3, 1), (2, 4, 1), (2, 5, 1), (3, 4, 1), (4, 5, 1)]
NEIGHBOURS FOR EACH NODE IN A GRAPH
1 : [2, 5]
2 : [1, 3, 4, 5]
3 : [2, 4]
4 : [2, 3, 5]
5 : [1, 2, 4]
"""
    #Assert statement to test and verify against the output.
    assert output.strip() == expected_output.strip(), f"Output didn't match against the expected!\nOutput:\n{output}\nHere is the Expected Outpt:\n{expected_output}"

    print(output)

if __name__ == "__main__":
    main()



#Original Comment
'''
EXPECTED OUTPUT:

GRAPH
{1: [(2, 1), (5, 1)], 2: [(1, 1), (3, 1), (4, 1), (5, 1)], 3: [(2, 1), (4, 1)], 4: [(2, 1), (3, 1), (5, 1)], 5: [(1, 1), (2, 1), (4, 1)]}

LIST OF NODES
[1, 2, 3, 4, 5]

LIST OF EDGES
[(1, 2, 1), (1, 5, 1), (2, 3, 1), (2, 4, 1), (2, 5, 1), (3, 4, 1), (4, 5, 1)]

NEIGHBOURS FOR EACH NODE IN A GRAPH
1 : [2, 5]
2 : [1, 3, 4, 5]
3 : [2, 4]
4 : [2, 3, 5]
5 : [1, 2, 4]
'''

