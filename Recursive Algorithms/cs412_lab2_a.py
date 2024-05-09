# cannot use binary search
# find the split point and then split into two parts
    # sort each part and then apply binary search to each part which would run in
    # log(n) running time

# splitting will have runtime of logn
# querying the circular array will run in 2logn time
# overall this algorithm will take logn time

# how can you split circular array into two halves:
    # use binary search to find split point
    # Case 1: array is {8, 10, 1, 3, 6, 7}
    # midpoint is 1; to find midpoint, use 0 + 5 / 2 index
    # after finding the midpoint, decide whether to split at that midpoint or not
        # if yes, terminate
        # if not, go left or right recursively
        # want to compare midpoint with values to the left and right of it
        # if the left neighbor is larger than the midpoint, you can decide to split
        # at that midpoint; after splitting, there should be two lists: [0:2] and [2: ]


    # case 2: {1, 3, 6, 7, 8, 10}
    # if array is already sorted (can compare leftmost and rightmost values),
    # no need to find midpoint

    # case 3: {10, 1, 3, 6, 7, 8}
    # lets say midpoint is 3; its smaller than right neighbor and last element in
    # the array; its larger than its left neighbor so split [0:1] into own list
    # find midpoint of smaller array {10, 1}


#
# Input: Array arr of values and search key
# Output: The index of key in the array arr, if present, or -1 otherwise
# Coded by: Duan Bowers
#
# Searches an array of a sorted array arr for an element key.
# The array is the array(subarray) starting at index low and ending
# on index high(inclusive).

"""
    name: Alex Karapetkov
    
"""

def circularBinarySearch(arr, low, high, key):

    # If the array is empty, return -1
    if high < low:
        return -1

    # Get the mid point index of the array with low to high
    mid = (low + high) // 2

    # if arr[mid] is the key, return mid point.
    if key == arr[mid]:
        return mid

    # if the left half is sorted and the key is within that range
    if arr[low] <= arr[mid]:
        # check if the key is within the left half 
        if arr[low] <= key <= arr[mid]:
            return circularBinarySearch(arr, low, mid - 1, key)
        # if not, search the right half
        else:
            return circularBinarySearch(arr, mid + 1, high, key)
    
    # if the right half is sorted and the key is within that range
    elif arr[mid] <= arr[high]:
        # check if the key is within the right half
        if arr[mid] <= key <= arr[high]:
            return circularBinarySearch(arr, mid + 1, high, key)
        # if not, search in the left half
        else:
            return circularBinarySearch(arr, low, mid - 1, key)

    # if the key lies in the unsorted part, search both halves
    else:
        left_search = circularBinarySearch(arr, low, mid - 1, key)
        if left_search != -1:
            return left_search
        else:
            return circularBinarySearch(arr, mid + 1, high, key)

def main():
    # input circularly sorted list of numbers
    arr = list(map(int, input().strip().split()))

    # input query integer
    key = int(input().strip())

    # perform circular binary search and print the index
    index = circularBinarySearch(arr, 0, len(arr) - 1, key)
    print(index)
    
    pass

if __name__ == "__main__":
    main()


