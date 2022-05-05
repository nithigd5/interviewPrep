from collections import deque
from Graph import Graph
# Function to perform DFS traversal on the graph on a graph
 
    
def DFS(graph, v, discovered):
 
    discovered[v] = True            # mark the current node as discovered
    print(v, end=' ')               # print the current node
 
    # do for every edge (v, u)
    for u in graph.adjList[v]:
        if not discovered[u]:       # if `u` is not yet discovered
            DFS(graph, u, discovered)
 
 
if __name__ == '__main__':
 
    # List of graph edges as per the above diagram
    edges = [
        # Notice that node 0 is unconnected
        (1, 2), (1, 7), (1, 8), (2, 3), (2, 6), (3, 4),
        (3, 5), (8, 9), (8, 12), (9, 10), (9, 11)
    ]
 
    # total number of nodes in the graph (labelled from 0 to 12)
    n = 13
    n = int(input())
    edges = []
    inp = input()
    while(inp):
        edges.append(tuple(map( int, inp.split(" "))))
        inp = input()
    # build a graph from the given edges
    graph = Graph(edges, n)
 
    # to keep track of whether a vertex is discovered or not
    discovered = [False] * n
 
    # Perform DFS traversal from all undiscovered nodes to
    # cover all connected components of a graph
    for i in range(n):
        if not discovered[i]:
            DFS(graph, i, discovered)