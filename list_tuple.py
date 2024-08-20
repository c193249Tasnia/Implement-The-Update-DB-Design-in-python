# Advanced Python: Lists and Tuples

"""
Tasnia sharmin
ID: C193249
Email: c193249@ugrad.iiuc.ac.bd
"""

# Section 1: Python Lists
# -----------------------
# Lists in Python are ordered, mutable (changeable), and allow duplicate elements.

### Assignment 1: Create a 2D list representing a 3x3 matrix and perform operations like accessing, modifying, and iterating through it.
# Write your code below:
matrix = [[4, 1, 10], [3, 15, 2], [7, 5, 9]]
value1 = matrix[2][2]
value2 = matrix[1][0]
print("The result is: ",value1,"and ",value2)

matrix[2].append(1) #appending a new value in row 3
print("After Appending a value: ")
for row in matrix:
    print(row)
    
new_row = [10, 11, 12] #appending a new row
matrix.append(new_row)
print("After Appending a new row: ")
for row in matrix:
    print(row)

matrix = [[4, 1, 10], [3, 15, 2], [7, 5, 9]]
new_col = [2, 2, 2]
matrix.append(new_col) #appending a new coloum
print("After Appending a new coloum: ")
for row in matrix:
    print(row)
    
matrix = [[4, 1, 10], [3, 15, 2], [7, 5, 9]]
matrix[1].insert(2, 3)
print("After inserting: ")
for row in matrix:
    print(row)

matrix[1].remove(3)
print("After removing: ")
for row in matrix:
    print(row)
    
matrix[0].pop()
print("After poping: ")
for row in matrix:
    print(row)

matrix = [[4, 1, 10], [3, 15, 2], [7, 5, 9]]
sort_matrix = [sorted(row) for row in matrix] #sort in row-wise
print("After sorting row-wise: ")
for row in sort_matrix:
    print(row)


transpose_matrix = list(zip(*sort_matrix)) # Transposing the matrix to sort columns
sort_transpose_matrix = [sorted(column) for column in transpose_matrix] # Sorting each column individually
new_sort_matrix = list(zip(*sort_transpose_matrix)) # Transposing the sorted matrix back to original form
print("After sorting coloum-wise: ")
for row in new_sort_matrix:
    print(row)
    
# duplicate a matrix
matrix = [[4, 1, 10], [3, 15, 2], [7, 5, 9]]
duplicate_matrix = matrix
duplicate_matrix[2].append(16)
print("matrix id", id(matrix), "duplicate_matrix id: ", id(duplicate_matrix))
print("Duplicate List: ")
for row in duplicate_matrix:
    print(row)
print("Matrix: ")
for row in matrix:
    print(row)

# copy a matrix
matrix = [[4, 1, 10], [3, 15, 2], [7, 5, 9]]
matrix_copy = [row[:] for row in matrix] # here matrix.copy() can't be use bcz it creates a shallow copy of the matrix
matrix_copy[0].append(8)
print("Copy List: ")
for row in matrix_copy:
    print(row)
   
print("Matrix: ")
for row in matrix:
    print(row)

#iterating each number
matrix = [[4, 1, 10], [3, 15, 2], [7, 5, 9]] 
print("After iteration by row: ")
for row in matrix:
    for value in row:
        print(value, end=' ')
    print()

# Combining matrix
matrix1 = [[4, 1, 5], [3, 1, 2], [7, 5, 9]]
matrix2 = [[3, 6, 2], [2, 0, 3]]
combined_matrix = matrix1 + matrix2
print("combined matrix: ")
for row in combined_matrix:
    print(row)
# Section 2: Python Tuples
# ------------------------
# Tuples are ordered collections like lists but are immutable (cannot be changed after creation).

# Assignment 2: Create a tuple with mixed data types and demonstrate its potential use cases in data structures like dictionaries.
# Write your code below:
mixed_tuple = ("nim",29,"Chittagong",7.897)
tuple_dict={mixed_tuple:"My profile"}
print("Name:", mixed_tuple[0])
print("ID:", mixed_tuple[1])
print("Address:", mixed_tuple[2])
print("CGPA:", mixed_tuple[3])
print("Title:", tuple_dict[mixed_tuple])

# Section 3: Advanced Applications
# --------------------------------
# Dealing with more complex list and tuple structures for real-world applications.

# Example 3: Advanced List Operations
# Filtering with list comprehensions

# Assignment 3: Create a list of tuples, where each tuple contains a student's name and their grade. Sort this list by grades.
# Write your code below:
details = [
    ("nim", 85),
    ("jack", 90),
    ("anj", 75),
    ("me", 95),
    ("sahi", 80)]

sorted_details = sorted(details,key=lambda x: x[1],reverse=True) # grades will apper in descending order
print(sorted_details)
#for student, grade in sorted_details:
    #print("{}:{}".format(student, grade))

# Congratulations on completing the advanced section on Python lists and tuples!
# Review the assignments, try to solve them, and check your understanding of these versatile data structures.
