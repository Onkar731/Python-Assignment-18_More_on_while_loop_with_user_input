"""
Write a python script to print first "N" even natural numbers
"""

# taking a values from the user
n = int(input("Enter a number : "))

# defining a counter variable for iteration
i = 1

# printing first "n" even natural numbers using while loop
while i <= n :
    print(i*2, end=' ')
    i += 1