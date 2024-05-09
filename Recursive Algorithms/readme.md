Problem 1
A list A[0..(n-1)] is circularly sorted if there is an index i such that the subarray A[(i+1)..(n-1)] concatenated to the subarray A[0..i] is a sorted list. For example {7, 8, 10, 1, 2, 3, 4} is circularly sorted, since the subarray A[3..6] concatenated with the subarray A[0..2] is the array {1, 2, 3, 4, 7, 8, 10}, which is sorted. Your task is to write a recursive algorithm, which given a a circularly sorted array with no duplicate values and a query integer q determines the index of q in the array if it exists, or -1 otherwise. Your algorithm should run in O(log n) time.

Input
The input will consist of two lines. The first line contains a circularly sorted, space separated list of numbers. The second line contains a single query integer. 

Output
You should output the index of the query integer (indexing from 0) in the list, if it exists, or -1 if it does not exist in the list.

Problem 2
An inversion in an array A[1..n] is a pair of indices (i, j) such that i < j and A[i] > A[j]. The number of inversions in an n-element array is between 0 (if the array is sorted) and 
(if the array is sorted backwards). In this problem you will write code to count the number of inversions in an n-element array in O(n log n) time. Hint:  Make modifications to Mergesort.  Here is a merge sort implementation in Python for you to start experimenting: mergesort.pyDownload mergesort.py

Input
The input will be a single line containing the numbers of the input array separated by spaces. Each number will be an integer. 

Output
The output is a single number equal to the number of inversions in the list. 
