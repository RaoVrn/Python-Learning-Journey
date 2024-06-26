# Input the elements of a tuple and sort them

# Method-I


# Initialize an empty list to store the elements
list_version = []  # Note: tuples are immutable, so we use a list instead

# Ask the user to input the number of elements in the list
n = int(input("Enter the number of elements in the list: "))

# Loop through the range of numbers from 0 to n-1
for i in range(0, n):
    # Ask the user to input each element, and append it to the list
    element = input("Enter element {}: ".format(i+1))
    list_version.append(element)

# Sort the list in-place
list_version.sort()
sorted_tuple = tuple(list_version)  # Convert the sorted list back to a tuple
print("The sorted tuple is:", sorted_tuple)

"""

# Method-II

# Input the elements of a tuple and sort them

# Initialize an empty tuple to store the elements
tuple = ()  # Note: tuples are immutable, so we can't sort them in-place

# Ask the user to input the number of elements in the tuple
n = int(input("Enter the number of elements in the tuple: "))

# Loop through the range of numbers from 0 to n-1
for i in range(0, n):
    # Ask the user to input each element, and append it to the tuple
    element = input("Enter element {}: ".format(i+1))
    tuple += (element,)  # Note: this creates a new tuple, it doesn't modify the original

# Convert the tuple to a list, sort it, and then convert it back to a tuple
list_version = list(tuple)
list_version.sort()
sorted_tuple = tuple(list_version)
print("The sorted list is:", list_version)  # Note: you printed the wrong variable
"""