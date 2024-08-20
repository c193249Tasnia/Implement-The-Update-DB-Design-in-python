# Python Conditional Logic: Mastering Control Flow

"""
tasnia sharmin
ID: C193249
Email: c193249@ugrad.iiuc.ac.bd
"""

# Section 1: Basic Conditional Statements
# ---------------------------------------
# The `if` statement is the simplest form of control flow, allowing for conditional execution of code blocks.

# Assignment 1: Write a Python script that determines if a number is positive, negative, or zero using if-elif-else.
# Write your code below:

num = float(input("Enter a number: "))

if num > 0:
    print("This number is positive.")
elif num < 0:
    print("This number is negative.")
else:
    print("This number is zero.")


# Section 2: Logical and Boolean Operations
# -----------------------------------------
# Logical operators (and, or, not) are used to combine conditional statements.

# Assignment 2: Create a script that checks if a person is eligible for a student discount based on age and student status.
# Write your code below:

# Input age and student status
age = int(input("Enter your age: "))
is_student = input("Are you a student (yes/no)?: ").lower()

if age < 25 and is_student == "yes":
    print("You are eligible for a student discount.")
else:
    print("You are not eligible for a student discount.")


# Section 3: Real-World Applications
# -----------------------------------
# Applying conditional logic to solve real-world problems.

# Assignment 3: Write a script that simulates a basic login system. Check username and password correctness.
# Write your code below:

# Dictionary to store usernames and passwords
user_credentials = {
    'nim': 'password123',
    'anju': 'qwerty987',
    'shams': 'letmein456'
}

def login(username, password):
    if username in user_credentials and user_credentials[username] == password:
        return True
    else:
        return False

username = input("Enter your username: ")
password = input("Enter your password: ")

if login(username, password):
    print(f"Login successful! Welcome, {username}.")
else:
    print("Invalid username or password. Please try again.")


# Assignment 4: Implement a system that categorizes a day based on temperature and weather conditions.
# Use nested if-elif-else and logical operators to determine if it's a hiking day, a movie day, or a stay-home day.

temperature = 18  # in Celsius
weather = "cloudy"

if weather == "sunny":
    if temperature > 20:
        print("It's a great day for hiking.")
    elif temperature > 10:
        print("It's a pleasant day for a short walk.")
    else:
        print("It's sunny but chilly, better stay home.")
elif weather == "rainy":
    if temperature > 15:
        print("It's a good day to stay in and watch a movie.")
    else:
        print("It's rainy and cold, stay home and keep warm.")
else:
    print("Not ideal weather for outdoor activities, best to stay indoors.")

# Congratulations on completing the advanced section on Python conditional statements!
# Review the assignments, try to solve them, and check your understanding of control flow
