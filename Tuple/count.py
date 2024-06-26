# Write a program to count the number of students with the "A" grade in the following tuple.
# The tuple is: ["C", "D", "A", "A", "B", "B", "A"]

# Define a list of grades
list = ["C", "D", "A", "A", "B", "B", "A"]

# Initialize an empty tuple (not necessary, as we can directly convert the list to a tuple)
students = ()

# Convert the list to a tuple
students = tuple(list)

# Count the number of occurrences of "A" in the tuple
count = students.count("A")

# Print the result
print("The numbers of students with 'A' grade in the given list are:", count)