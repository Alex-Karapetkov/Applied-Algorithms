"""
    name: Alex Karapetkov

"""

"""
For this lab you will implement Dijkstra's algorithm. The main data structure you need to work with is the Priority Queue. The easiest way
to use it for Dijstra's algorithm is to push tuples (key, v) where key is the distance for the vertex v. Heres's an example:


from queue import PriorityQueue

pq = PriorityQueue() # initialize 

pq.put((10,"blue")) # push a few values on the pq
pq.put((3, "green"))
pq.put((5, "purple"))
pq.put((11, "orange"))

while not pq.empty(): # pop in order (min queue)
    print(pq.get())

Since tuples compare by their first component and then break ties by their second, this implements a priority queue on the key values and 
breaks ties by which vertex has the "lower" string (in alpha order). In your implementation, you will be using integers as vertex IDs (and
ties in Dijkstra's algorithm can be broken arbitrarily.)

Important notice: There is no decrease key operation on a PriorityQueue, which is in the pseudocode for Dijkstra, but this is ok. If we already
have a vertex, say v, with a key value of k1 in the queue and we want to decrease its key to k2 < k1, we can simply add (k2, v) to the queue as
well. Yes, both are now in the queue, but this isn't a problem because (k2, v) will be popped before (k1, v). If we just keep track of which
vertices we are done with (like we do in DFS using the marked structure), then we can just ignore any values we pop off the queue that correspond
to vertices that have already been processed. This does not effect the runtime of the algorithm but does increase its memory footprint.

Your Task:
You will implement a program that loads a weighted, directed graph with n vertices and m edges and performs q shortest path queries. For each
query your program should report the length of the shortest path between two nodes if one exists or "Impossible" if a path does not exist.

Input:
The input consists of a first line containing the numbers n, m, and q separated by spaces. The number of vertices in the input graph is n and
they are numbered 0, 1, ..., n-1. The next m lines give the edges of the graph in the form u v w denoting an edge from vertex u to vertex v
with weight w. All weights are positive and will be integers. The final lines of input consist of q query lines of the form s t where the 
query is asking for the length of the shortest path from s to t in the graph. 

Output:
The code should output one line per query with the length of the shortest path if a path exists or "Impossible" if no path exists.
"""

from queue import PriorityQueue

def dijkstra(graph, v0):
    n = len(graph)

    # start with large initial distance, representing distance of infinity for all
    # vertices except start vertex
    distance = [float('inf')] * n
    distance[v0] = 0

    # intialize priority queue
    pq = PriorityQueue()
    # add start index to pq with priority of 0
    pq.put((0, v0))

    # create list to keep track of which vertices have been processed already
    processed = [False] * n

    # pop in order (min queue)
    while not pq.empty():
        # remove vertex with smallest distance
        d, u = pq.get()
        # if vertex has already been processed, exit loop
        if processed[u]: continue

        # go through all edges from current vertex to adjacent vertices
        for v, w in graph[u]:
            # if distance to neighbor can be improved
            if distance[u] + w < distance[v]:
                # update distance and add to pq
                distance[v] = distance[u] + w
                pq.put((distance[v], v))

        # update processed vertices list
        processed[u] = True
    return distance

def main():
    
    # get n, m, and q inputs
    n, m, q = map(int, input().split())

    # create 2D array to represent graph and hold each vertex
    graph = [[] for _ in range(n)]
    
    # get next m lines of input (u v w)
    for _ in range(m):
        u, v, w = map(int, input().split())
        # store each vertex along with its edge and weight in graph
        graph[u].append((v, w))

    results = []

    # get q query lines of input (s t)
    for _ in range(q):
        s, t = map(int, input().split())
        
        # call dijkstra's algorithm on each query line
        shortest_path = dijkstra(graph, s)
        results.append(shortest_path[t] if shortest_path[t] != float('inf') else "Impossible")

    for result in range(len(results)):
        print(results[result])
    pass

if __name__ == "__main__":
    main()
