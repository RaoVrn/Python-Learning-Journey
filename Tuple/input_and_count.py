# Write a program to count the number of students with the "A" grade in the tuple inputed from the user.

# Initialize an empty tuple to store student information
tuple = ()

# Ask the user to input the number of students
n = int(input("Enter the number of elements in the list: "))

# Loop through each student
for i in range(0, n):
    # Ask the user to input student name and grade (e.g., "A", "B", etc.)
    element = input("Enter student name and grade (e.g., A, B, etc...): ")
    # Add the input to the tuple
    tuple = tuple + (element,)

# Count the number of "A" grades in the tuple (Note: This will only count exact matches of "A", not grades like "A+", "A-", etc.)
count = tuple.count("A")

# Print the result
print('The number of students with the "A" grade in the tuple', tuple, 'are:', count)