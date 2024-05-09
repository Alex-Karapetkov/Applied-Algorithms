"""
    name: Alex Karapetkov

"""

def merge_sort(arr):
    # Base case: if the array has one or fewer elements, its already
    # sorted
    if len(arr) <= 1:
        return arr, 0

    # split the array into two halves
    mid = len(arr) // 2
    left_half, left_inversions = merge_sort(arr[:mid])
    right_half, right_inversions = merge_sort(arr[mid:])

    # merge the two sorted halves and count inversions
    merged_arr, merge_inversions = merge(left_half, right_half)

    # return the merged array and the total number of inversions
    return merged_arr, left_inversions + right_inversions + merge_inversions

def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0
    inversions = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            # if element from the right array is smaller, its an
            # inversion
            merged.append(right[right_index])
            right_index += 1
            # increment inversions by the number of remaining elements
            # in the left array
            inversions += len(left) - left_index

    # append remaining elements from the left and right arrays
    merged.extend(left[left_index:])
    merged.extend(right[right_index:])

    return merged, inversions

def count_inversions(arr):
    _, inversions = merge_sort(arr)
    return inversions

# All modules for CS 412 must include a main method that allows it
# to imported and invoked from other python scripts
def main():
    # input parsing
    arr = list(map(int, input().strip().split()))

    # count inversions and print the result
    inversions = count_inversions(arr)
    print(inversions)

    pass

if __name__ == "__main__":
    main()
