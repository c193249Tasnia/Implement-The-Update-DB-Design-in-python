# Python Basics: Variables and Data Types

tasnia sharmin
ID: C193249
Email: c193249@ugrad.iiuc.ac.bd
"""
# Section 1: variables.
#----------------------

# Assignment 1: Create two variables, one holding a number and the other holding your name. Then print both.
# Write your code below:
id = 29;
name = "nim"

print("ID:",id)
print("Name:", name)

# Section 2: Data Types.
# ---------------------

# Assignment 2: Create variables of different types and use the type() function to check their types.
# Write your code below:
a = 10               
b = 2.156            
c = "Hey!"        
d = False
e = 3.39e124 
f = 3+2j           

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))


# Section 3: Variable Naming Conventions and Industry Standards
# -------------------------------------------------------------
#Example 3: Good and Bad Variable Names
#good_name = "John"
#bad_name = dyrotth
#2bad = 42  # This will raise a SyntaxError because variable names cannot begin with a number.

# Assignment 3: Fix the bad variable name above and create three more variables with good naming practices.
# Write your code below:
bad = 42 #Fix the bad variable name above mentioned
birth_of_month = "november"
Person1_fees = 30000.000
_future_tense = "I will meet"

print("Fixed variable: ",bad)
print("Birth Month = ",birth_of_month)
print("First Person Fees: ",Person1_fees)
print("Write a future Tense: ",_future_tense)

# Section 4: Python's Dynamic Typing
# ----------------------------------
# Python is dynamically typed, which means you don’t have to declare the type of variable while declaring it.
# Example 4: Dynamic Typing
# Assignment 4: Create a variable, assign it a value of one type, then reassign it to a different type and print both.
# Write your code below:
data = 30.311
print("Type of variable", type(data), end=" ")
print(data) 

data = "what do you want"
print("Type of variable", type(data), end=" ")
print(data)


# Congratulations on completing this part of the Python workshop!
# Review the assignments, try to solve them, and check your understanding of variables and data types.
