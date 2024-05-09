Description
In this lab you will develop a recursive algorithm for the palindrome partition counting problem. 

A palindrome is a string of letters that is the same backwards as forwards. For example, "racecar", "eevee", and "12321" are all palindromes.  A string with a single character is trivially a palindrome. 

A palindromic partition of a string is a partition of the string into substrings whose concatenation is equal to the original string, but such that every substring is itself a palindrome. 

For example, the string, "seeks" can be broken up into the palindrome partition ["s", "ee", "k", "s"] or as ["s", "e", "e", "k", "s"]. Your task is to design and implement a recursive algorithm that counts the number of palindromic partitions of a given string. 

Input
Your input will begin with a single line containing a nonnegative integer n followed by exactly n lines each of which contains an input string. 

Output
You should output exactly n lines, one for each input string with each ending in a newline character. The value of each line should be the number of unique palindromic partitions that can be made with the input string.
