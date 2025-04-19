"""
    1. Even or Odd Checker
Ask the user for a number and tell them whether it's even or odd.
Example:
Input: 7
Output: 7 is an odd number.

"""

x = int(input("Enter a number\n"))
if x%2 == 0:
    print('This number is even')
else: print('This number is odd')