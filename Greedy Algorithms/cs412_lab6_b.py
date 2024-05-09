"""
    name: Alex Karapetkov

"""

def fractional_knapsack(capacity, items):

    # convert item values to floats
    for item in items:
        item[1] = float(item[1]) # value
        item[2] = float(item[2]) # weight
    
    # sort items by descending value/weight ration
    items.sort(key=lambda x: x[1]/x[2], reverse=True)

    total_value = 0.0
    fractions = [0]*len(items)

    for i in range(len(items)):
        if capacity > items[i][2]:
            fractions[i] = 1
            total_value += items[i][1]
            capacity -= items[i][2]
        else:
            fractions[i] = capacity / items[i][2]
            total_value += items[i][1]*capacity / items[i][2]
            break

    return fractions, total_value


def main():
    # get the capacity from the user
    capacity = float(input())

    # get the number of items from the user
    n = int(input())

    # get the items from the user
    items = []
    for i in range(n):
        item = input().split()
        items.append(item)

    fractions, total_value = fractional_knapsack(capacity, items)

    # print the items in the knapsack
    for i in range(len(items)):
        print(f"{items[i][0]}({items[i][1]*fractions[i]:.2f}, {items[i][2]*fractions[i]:.2f}) ", end="")
    print()

    # print the total value
    print(f"{total_value:.1f}")
    pass

if __name__ == "__main__":
    main()
