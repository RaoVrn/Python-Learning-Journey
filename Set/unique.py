# You are given a list of subjects for students. Assume one classroom is required for 1 subject. How many classrooms are needed by all students.

# The list of subjects, where duplicates represent multiple students taking the same subject
list = ["python", "java", "C++", "python", "javascript", "java", "python", "java", "C++", "C"]

# Convert the list to a set, which automatically removes duplicates
set = set(list)

# Print the number of unique subjects, which represents the number of classrooms needed
print("The number of classrooms are needed by all students are:", len(set))