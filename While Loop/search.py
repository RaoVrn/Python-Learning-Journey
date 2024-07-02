# Search for a number x in this tuple using loop:
# [1, 4, 9, 16, 25, 36, 49, 64, 81,100]



# Method-I


# Define a list of numbers
list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# Convert the list to a tuple
tuple = tuple(list)

# Prompt the user to enter a number to find in the tuple
x = int(input("Enter the number to find: "))

# Initialize the index counter
i = 0

# Start a while loop that continues until i exceeds the length of the tuple
while (i <= len(tuple)):
    # Check if the current element in the tuple is equal to the input number
    if (tuple[i] == x):
        # If the number is found, print the index and break the loop
        print("The number", x, "is found at index", i)
        i = i + 1  # Increment the index (this line is actually unnecessary since the loop breaks here)
        break
    else:
        # If the number is not found at the current index, print a message
        print("The number is not found in the tuple")
        i = i + 1  # Increment the index to check the next element






# Method-II


# Define a tuple containing a series of numbers
tuple_numbers = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

# Prompt the user to enter a number to search for in the tuple
x = int(input("Enter a number to search: "))

# Initialize a variable to keep track of the index
index = 0

# Initialize a flag to indicate whether the number was found
found = False

# Loop through the tuple to search for the number
while index < len(tuple_numbers):
    # Check if the current element is the number we're searching for
    if tuple_numbers[index] == x:
        # If the number is found, set the flag to True and break out of the loop
        found = True
        break
    # Increment the index to move to the next element
    index += 1

# Check the flag to determine if the number was found
if found:
    # If the number was found, print a success message
    print(f"The number {x} is found in the tuple.")
else:
    # If the number was not found, print a failure message
    print(f"The number {x} is not found in the tuple.")
