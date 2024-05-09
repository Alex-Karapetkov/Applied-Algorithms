"""
    name: Alex Karapetkov
    CS 412 Coding Homework 8: Arbitrages
"""

import math

def bellman_ford(graph, start):
    # initialize distances to infinity and predecessor to None
    # distances dictionary holds shortest distances from start to each node
    distances = {node: float('inf') for node in graph}
    # predecessor dict used to reconstruct shortest path
    predecessor = {node: None for node in graph}
    distances[start] = 0

    # Repeatedly relax edges
    for _ in range(len(graph) - 1):
        for node in graph:
            for adjacent, weight in graph[node]:
                # check if distance from start to adj is shorter than current distance
                if distances[node] + weight < distances[adjacent]:
                    distances[adjacent] = distances[node] + weight
                    predecessor[adjacent] = node

    # check for negative weight cycles
    for node in graph:
        for adjacent, weight in graph[node]:
            # if shorter path found, indicating neg weight cycle, return True with start node
            if distances[node] + weight < distances[adjacent]:
                return True, node
    return False, None

# function used to find arbitrage cycles based on exchange rates provided
def find_arbitrage(exchange_rates):
    # build the graph to represent exchange rates
    graph = {}
    for c_in, c_out, rate in exchange_rates:
        # if c_in not in graph, initialize empty list for it
        if c_in not in graph:
            graph[c_in] = []
        # add tuple with ending exchange rate and negative log of rate
        graph[c_in].append((c_out, -math.log(rate)))

    # run the Bellman Ford algorithm on graph and first currency
    cycle, start_currency = bellman_ford(graph, exchange_rates[0][0])

    # check if negative cycle was detected
    if cycle:
        # backtrack to find the cycle
        cycle = [start_currency]
        node = start_currency
        while True:
            # update node to next node in cycle
            node = graph[node][0][0]
            if node == start_currency:  # complete cycle
                break
            cycle.append(node)

        # Format the cycle and calculate factor increase
        exchanges = " => ".join(cycle + [start_currency])   # add start currency at end
        # sum negative logs of exchange rates along cycle
        factor_increase = math.exp(-sum(graph[node][0][1] for node in cycle))

        return exchanges, factor_increase
    else:
        return "No Arbitrage Detected", 0.0

def main():
    # get input
    num_rates = int(input().strip())
    exchange_rates = []
    for _ in range(num_rates):
        c_in, c_out, rate = input().split()
        rate = float(rate)
        # add starting currency, ending currency, and exchange rate as tuple to list
        exchange_rates.append((c_in, c_out, rate))

    exchanges, factor_increase = find_arbitrage(exchange_rates)

    # print output
    if exchanges != "No Arbitrage Detected":
        print("Arbitrage Detected")
        print(exchanges)
        print("{:.5f} factor increase".format(factor_increase))
    else:
        print(exchanges)

    pass

if __name__ == "__main__":
    main()
