# WAP to enter marks of n subjects from the user and store them in a dictionary. Start with an empty dictionary & add one by one. Use subject name as key & marks as value.WAP to enter marks of 3 subjects from the user and store them in a dictionary. Start with an empty dictionary & add one by one. Use subject name as key & marks as value.

# Initialize an empty dictionary to store the marks
dict_marks = {}

# Ask the user to input the number of subjects
n = int(input("Enter the number of subjects: "))

# Loop through the range of the number of subjects
for i in range(0, n):
    # Input the subject name from the user
    subject = input("Enter the subject: ")
    
    # Input the marks for the subject from the user
    marks = int(input("Enter the marks: "))
    
    # Add the subject and marks to the dictionary
    dict_marks[subject] = marks

# Print the resulting dictionary
print("The dictionary is:", dict_marks)