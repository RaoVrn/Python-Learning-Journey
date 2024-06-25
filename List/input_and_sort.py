# Input the elements of a list and sort them

# Initialize an empty list to store the elements
list = []

# Ask the user to input the number of elements in the list
n = int(input("Enter the number of elements in the list: "))

# Loop through the range of numbers from 0 to n-1
for i in range(0, n):
    # Ask the user to input each element, and append it to the list
    element = input("Enter element {}: ".format(i+1))
    list.append(element)

# Sort the list in-place
list.sort()
print("The sorted list is:", list)