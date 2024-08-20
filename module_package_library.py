# Python Modules, Packages, Libraries, and Pip: In-Depth Guide

"""
tasnia sharmin
ID: C193249
Email: c193249@ugrad.iiuc.ac.bd
"""
# Section 1: Modules
# ------------------
# A module in Python is a file containing Python code such as functions, classes, or variables. Modules help in organizing and reusing code.

# Section 2: Packages
# -------------------
# A package is a directory containing multiple modules. It typically contains an `__init__.py` file, which indicates that the directory is a package.

# Section 3: Libraries
# --------------------
# A library in Python is a collection of modules and packages that provides specific functionality, like data analysis, plotting, or machine learning.

# Assignments
# -----------

# Assignment 1: Create a simple package with at least two modules, each containing one function.

# Assuming the package structure is:
# Packages/
# ├── __init__.py
# ├── module1.py
# └── module2.py

# module1.py
def home():
    return "Welcome to your home!"

# module2.py
def hobby():
    return "I love playing MLBB!"

# Main script that imports the package and uses the functions
from Packages import module1, module2

print(module1.home())
print(module2.hobby())

# Assignment 2: Use pip to install any library that is new to you and write a small script to explore its functionality.

# Using matplotlib for plotting (if not installed, use pip install matplotlib)
import matplotlib.pyplot as plt

# Data for plotting
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# Creating a simple line plot
plt.plot(x, y)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Simple Line Plot')
plt.show()

# Congratulations on completing the section on Python's modules, packages, libraries, and pip!
# Review the assignments, try to solve them, and check your understanding of these essential Python features.
