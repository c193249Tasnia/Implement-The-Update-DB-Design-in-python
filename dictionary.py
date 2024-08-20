# Advanced Python: Dictionaries

"""
Tasnia sharmin
ID: C193249
Email: c193249@ugrad.iiuc.ac.bd
"""

# Section 1: Dictionary Basics
# Dictionaries in Python are unordered collections that store data in key-value pairs.

# Assignment 1: Create a dictionary representing a student with keys like 'name', 'roll_number', 'grades' (a list of subjects and marks).
# Perform various operations like adding, removing, and modifying elements.
# Write your code below:

# Create a dictionary representing a student with keys like 'name', 'roll_number', 'grades'.

student = {
    'name': 'nim',
    'roll_number': 49,
    'grades': {'biology': 80, 'english': 90, 'math': 75}
}

print("Before:", student)

# Adding a new subject and grade
student['grades']['physics'] = 82

# Removing an existing subject and its grade
removed_value = student['grades'].pop('Math')

# Updating a subject's grade
student['grades']['physics'] = 90

print("After:", student)

# Section 2: Integrating Dictionaries with Lists and Tuples
# Create a dictionary where keys are student names and values are lists of grades.
# Calculate the average grade for each student.

student_grades = {
    'Nim': [80, 65, 75],
    'anju': [85, 70, 85],
    'shams': [60, 80, 50]
}

average_grades = {}
for student, grades in student_grades.items():
    average_grade = sum(grades) / len(grades)
    average_grades[student] = average_grade

print("\nAverage Grades:")
for student, average_grade in average_grades.items():
    print(f"{student}: {average_grade:.2f}")


# Section 2: Integrating Dictionaries with Lists and Tuples
# Dictionaries can be used with lists and tuples to create complex data structures.

# Assignment 2: Create a dictionary where keys are student names and values are lists of grades. Calculate the average grade for each student.
# Write your code below:
student_grades = {
    'nim': [80, 65, 75],
    'anju': [85, 70, 85],
    'shams': [60, 80, 50]
}

average_grades = {}
for student, grades in student_grades.items():
    average_grade = sum(grades) / len(grades)
    average_grades[student] = average_grade

print("Average Grades:")
for student, average_grade in average_grades.items():
    print(f"{student}: {average_grade:.3f}")
    
# Congratulations on completing the advanced section on Python dictionaries!
# Review the assignments, try to solve them, and check your understanding of this powerful data structure.
