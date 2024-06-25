# WAP to check if a list contains a palindrome of elements.

# Initialize an empty list
list = []

# Ask the user to enter the number of elements in the list
n = int(input("Enter the number of elements in the list: "))

# Use a while loop to get each element from the user and add it to the list
while (n > 0):
    # Get an element from the user
    element = input("Enter the element: ")
    # Add the element to the list
    list.append(element)
    # Decrement the counter
    n -= 1

# Create a copy of the original list
new_list = []
new_list = list.copy()

# Reverse the copy of the list
new_list.reverse()

# Check if the original list is the same as the reversed list
if(list == new_list):
    # If they are the same, print that the list is a palindrome
    print("The list:", list, "is a Palindrome")
else:
    # If they are not the same, print that the list is not a palindrome
    print("The list:", list, "is not a Palindrome")