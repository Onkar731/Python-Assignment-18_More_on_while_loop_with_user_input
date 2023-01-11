"""
Write a python script to print first 10 multiples of N
"""

# taking a values from the user
n = int(input("Enter a number : "))

# defining a counter variable for iteration
i = 1

# printing first "n" natural numbers using while loop
while i <= 10 :
    print(n*i, end=' ')
    i += 1