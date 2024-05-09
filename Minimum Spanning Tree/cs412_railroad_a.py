"""
    name: Alex Karapetkov
"""

'''
Specification:
There are n cities that want to create a shared train network so that each pair of cities is connected by rail to each of the other cities.
The cost of laying track is directly proportional to the distance between two cities. The cost to lay one mile of railroad track is $1M.
Your task is to determine the lowest cost possible for laying the track so that all the cities are connected.

Input:
A single line containing the number n of cities followed by n city coordinate lines. Each of the coordinate lines is a pair of floating
point numbers x y giving the coordinates of the cities on a square grid (for this problem you may assume the earth is flat and that the
units of the grid structure are given in miles).

Output:
The minimum amount of money (in millions) that must be spent to create the railroad network. You can round this to a single decimal place.

Hints:
Can use connected components python module in code. It will produce labels for each of the vertices that correspond to their component. Will
need to use the adjacency list structure as suggested in order to use this code in its unmodified state.

If have already envisioned a way of representing this problem as a graph, draw the graph in the example on paper. How many edges does it have?

Adjacency list:
Augment your dictionary/set based adjacency structure to use a dictionary for the edges(instead of a set as before). This will allow you
to store the edge weights as the values of this second dictionary.

'''

import math
import heapq

# function finds distance between two cities using euclidean distance formula
def euclid_distance(city1, city2):
    x1, y1 = city1
    x2, y2 = city2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# function uses Prim's algorithm to find the MST of the graph with vertices being the cities and cost to connect
# cities is edge weight; total cost is sum of edge weights in MST
def min_cost(cities, n):
    # priority queue representing cost and city
    priority_queue = [(0, 0)]
    minimum_cost = 0
    visited = [False] * n

    while priority_queue:
        # get city with smallest cost
        cost, city = heapq.heappop(priority_queue)
        if not visited[city]:
            visited[city] = True
            # add cost of visiting city to total cost
            minimum_cost += cost
            # check neighboring cities of current city
            for adj_city in range(n):
                # put neighboring city in priority queue if hasn't been visited yet
                if not visited[adj_city]:
                    heapq.heappush(priority_queue, (euclid_distance(cities[city], cities[adj_city]), adj_city))
    
    return minimum_cost


def main():

    n = int(input())
    cities = []
    for _ in range(n):
        x, y = map(float, input().split())
        cities.append((x,y))

    total_min_cost = min_cost(cities, n)
    print(f"${total_min_cost:.1f}M")

    pass

if __name__ == "__main__":
    main()
