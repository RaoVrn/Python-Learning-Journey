# WAP to find the sum of first n numbers.


# Prompt the user to enter a number
n = int(input("Enter the value of n: "))

# Initialize a variable to store the sum of numbers
sum = 0

# Initialize a variable for iteration
i = 0

# Use a while loop to iterate from 0 to n
while (i <= n):
    # Add the current value of i to the sum
    sum += i
    # Increment i to move to the next number
    i += 1

# Print the sum of the first n numbers
print("Sum of first n numbers is:", sum)
