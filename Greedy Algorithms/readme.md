Greedy Algorithms
The knapsack problem is a well known, that when solved with a backtracking approach, has exponential complexity.  In this problem, you are given n items, each with item having a dollar value and a weight.  The knapsack can carry a maximum weight W.  The algorithm selects the subset of items with maximum value where the sum of the weights of the items does not exceed W.

Task 1: Develop pseudocode for 0-1 Knapsack
Develop pseudocode that solves this version of the knapsack problem (commonly known as the 0-1 knapsack problem, since you either take an item or do not take an item).  This can be a backtracking approach with recursion. 

Submit this as a text file (cs412_lab6_a_pseudo.txt).  It is OK if this code does not compile, but it should be fairly close.

 

Task 2: Code fractional knapsack problem
The fractional knapsack problem allows items to be broken into smaller pieces so that the total value of the items in the knapsack can be maximized as discussed in class.  Your method should run in O(n lg n) time. Submit this as a text file (cs412_lab6_b.py).

Input

Your input will begin with a single line containing a nonnegative integer weight w.  This is followed by a single line contains a nonnegative integer n followed by exactly n lines each of which contains a triple (String, real, real).  The first String is the item's name, the second is the dollar value of the item and the third is the item's weight.

Output

You should output exactly 2 lines.  The first line is the list of items in the knapsack with the value and amount (weight) of each item formatted as shown.  The order of the items should follow the ratio of the most expensive per unit weight.    The second line is the total value of the items in the knapsack.  
