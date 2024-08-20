# Python Functions: Comprehensive Guide

"""
tasnia sharmin
ID: C193249
Email: c193249@ugrad.iiuc.ac.bd
"""
# Section 1: Basic Functions
# --------------------------
# Functions are defined using the `def` keyword. They allow you to encapsulate code for reuse.

# Assignment 1: Write a function that calculates the factorial of a number and handles any potential errors.
def factorial(n):
    # Check if the input is a non-negative integer
    if not isinstance(n, int):
        print("Error: The input must be an integer.")
        return None
    elif n < 0:
        print("Error: The input must be a non-negative integer.")
        return None
    
    # Base case for factorial calculation
    if n == 0 or n == 1:
        return 1
    
    # Recursive case
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# Testing the function with different inputs
print("Factorial of 5:", factorial(5))  # Expected: 120
print("Factorial of -2:", factorial(-2))  # Expected: Error message
print("Factorial of 'abc':", factorial('abc'))  # Expected: Error message

# Congratulations on completing the basic section on Python functions!
# Review the assignments, try to solve them, and check your understanding of function concepts.
