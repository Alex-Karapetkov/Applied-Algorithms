'''
In this lab you will develop a recursive algorithm for the palindrome partition counting problem

A palindrome is a string of letters that is the same backwards as forwards. for example, "racecar", "eevee", and "12321" are all
palindromes. A string with a single character is trivially a palindrome.

A palindromic partition of a string is a partition of the string into substrings whose concatenation is equal to the original string,
but such that every substring is itself a palindrome.

For example, the string "seeks" can be broken up into the palindrome partition ["s", "ee", "k", "s"] or as ["s", "e", "e", "k", "s"]; your
task is to design and implement a recurisve algorithm that counts the number of palindromic partitions of a given string.

INPUT:
your input will begin with a single line containing a nonnegative integer n followed by exactly n lines each of which contains an input
string. 

OUTPUT:
You should output exactly n lines, one for each input string with each ending in a newline character. The value of each line should be the
number of unique palindromic partitions that can be made with the input string.

Sample Input:           Sample Output:
3                       
abc                     1
bcccb                   5
seeks                   2

Hints:
- As always, when devising a recursive backtracking algorithm, think of your output as a series of choices. Almost always you can get
to the recursive solution by having each recurisve call brute-force make all possible nect choice and use the recursion fairy to handle
the remaining choices.
    - what are the choices here? think about what you need to do to the string to turn it into a palindromic partition -- this will tell you
    exactly what a "choice" is in terms of producing palindromic partitions.
- Don't worry about speed here. You are almost certainly going to have a rather bad runtime. we'll fix this when we talk about dynamic 
programming
- you probably want to write a tiny helper predicate isPalindrome(s) that returns true if s is a palindrome and false otherwise; how can you
easily have a string evaluate to the reverse of itself? recall that slicing takes 3 values (start pos, end pos, step size); see website for
details: https://www.digitalocean.com/community/tutorials/how-to-index-and-slice-strings-in-python-3
'''

"""
    name: Alex Karapetkov

"""

def isPalindrome(s):
    # using slicing to read the string backwards
    return s == s[::-1]

def countPalindromes(s):
    # base case; empty string means to increase count by one for number of palindromic substrings
    if s == "":
        return 1
    # counter keeps track of number of palindromic substrings
    cnt = 0

    # loop that iterates over string s
    for i in range(1, len(s) + 1):
        # check if substring from start to current index is a palindrome
        if isPalindrome(s[0:i]):
            # if palindrome, have function call itself on remaining part of string and add result to counter
            cnt += countPalindromes(s[i:])
    return cnt

def main():
    n = int(input())
    words = [input() for _ in range(n)]
    num = 0

    for word in words:
        num = countPalindromes(word)
        print(num)

    pass

if __name__ == "__main__":
    main()
