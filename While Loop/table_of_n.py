# Print the multiplication table of a number n.

# Prompt the user to enter a number, and store it in the variable `n`.
n = int(input("Enter the number: "))

# Initialize a variable `i` to 1, which will be used as a counter.
i = 1

# Start a while loop that will continue to execute as long as `i` is less than or equal to 10.
while (i <= 10):
    # Print the multiplication of the user-input number `n` with the current value of `i`.
    print(n, "x", i, "=", n*i)
    # Increment `i` by 1 at the end of each iteration.
    i += 1