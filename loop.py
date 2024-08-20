
# Python Loops: Comprehensive Guide

"""
tasnia sharmin
ID: C193249
Email: c193249@ugrad.iiuc.ac.bd
"""

# Section 1: Basic Loop Usage
# ---------------------------
# For loops are ideal for iterating over sequences such as lists, tuples, or strings.

# Assignment 1: Write a script that processes a list of daily step counts. If any count is below a certain goal, print a motivational message.
step_counts = [8000, 12000, 9500, 7000, 14000, 6000]
goal = 10000

for steps in step_counts:
    if steps < goal:
        print(f"Keep going! You walked {steps} steps, just {goal - steps} more to reach your goal!")

# Assignment 2: Given a list of students and their exam results, write a loop that congratulates those who passed.
students = [
    {"name": "nim", "passed": True},
    {"name": "anju", "passed": False},
    {"name": "shams", "passed": True}
]

for student in students:
    if student["passed"]:
        print(f"Congratulations {student['name']}! You passed the exam.")

# Section 3: Advanced Loop Usage
# ------------------------------
# Nested loops and loops with conditional logic can handle more complex scenarios.

# Assignment 3: Create a script that processes a dictionary of classroom supplies, checking quantities and generating restock alerts if necessary.
classroom_supplies = {
    "markers": {"quantity": 12, "min_required": 20},
    "paper": {"quantity": 500, "min_required": 100},
    "erasers": {"quantity": 3, "min_required": 10}
}

for supply, details in classroom_supplies.items():
    if details["quantity"] < details["min_required"]:
        print(f"Alert: Low supply of {supply}. Only {details['quantity']} left, please restock!")
    else:
        print(f"{supply} quantity is sufficient.")

# Assignment 4: Create a script that categorizes a list of activities based on the weather conditions.
activities = ["Go for a run", "Watch a movie", "Visit a museum", "Have a picnic"]
weather_conditions = ["sunny", "rainy", "cloudy", "sunny"]

for i in range(len(activities)):
    if weather_conditions[i] == "sunny":
        print(f"{activities[i]} is perfect for a sunny day.")
    elif weather_conditions[i] == "rainy":
        print(f"{activities[i]} is great on a rainy day.")
    else:
        print(f"{activities[i]} works well in any weather.")

# Congratulations on completing the section on Python loops!
# Review the assignments, try to solve them, and check your understanding of loops in Python.



