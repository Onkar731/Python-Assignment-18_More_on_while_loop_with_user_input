"""
Write a python script to print cube of first "N" natural numbers
"""

# taking a values from the user
n = int(input("Enter a number : "))

# defining a counter variable for iteration
i = 1

# printing squares of first "n" natural numbers using while loop
while i <= n :
    print(i**3, end=' ')
    i += 1