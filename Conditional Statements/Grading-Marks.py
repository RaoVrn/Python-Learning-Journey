""" 
Grade students based on marks: 
marks >= 90, grade = “A”
90 > marks >= 80, grade = “B”
80 > marks >= 70, grade = “C”
70 > marks, grade = “D”
"""

marks = float(input("Enter the marks: "))

if (marks >= 90):
    print('grade = "A"')
    
elif (marks < 90 and marks >= 80):
    print('grade = "B"')
    
elif (marks < 80 and marks >= 70):
    print('grade = "C"')
    
elif (marks < 70):
    print('grade = "D"')