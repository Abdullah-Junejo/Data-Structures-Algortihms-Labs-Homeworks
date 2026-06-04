from helper_functions import *

'''
EXPECTED OUTPUT:

GRAPH
{1: [(2, 1)], 2: [(4, 1)], 3: [(1, 1), (2, 1)], 4: [(3, 1), (4, 1)]}

IN NEIGHBORS
1 : [3]
2 : [1, 3]
3 : [4]
4 : [2, 4]

OUT NEIGHBORS
1 : [2]
2 : [4]
3 : [1, 2]
4 : [3, 4]

ADJACENCY MATRIX
[[-1, 1, -1, -1], [-1, -1, -1, 1], [1, 1, -1, -1], [-1, -1, 1, 1]]

Sum of the in-degrees of all nodes, the sum of the out-degrees of all nodes and the total number of edges are all equal: True  
'''