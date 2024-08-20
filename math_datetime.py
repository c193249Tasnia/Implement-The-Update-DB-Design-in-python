# Python Math and Datetime Modules: In-Depth Guide
"""
tasnia sharmin
ID: C193249
Email: c193249@ugrad.iiuc.ac.bd
"""


# Section 1: Math Module

# ----------------------
# The math module provides access to various mathematical functions and constants.
import math

# Section 2: Datetime Module
# --------------------------
# The datetime module allows you to work with dates and times.

# Assignments
# -----------
# Assignment 1: Write a function that calculates compound interest using the formula:
# A = P(1 + r/n)^(nt)
# Where:
# P = principal amount (initial investment)
# r = annual interest rate (in decimal)
# n = number of times interest is compounded per year
# t = time in years
def calculate_compound_interest(principal, rate, time, compounds_per_year):
    amount = principal * (1 + rate / compounds_per_year) ** (compounds_per_year * time)
    interest = amount - principal
    return interest

# Example usage:
principal = 5000  # Principal amount in dollars
annual_rate = 0.08  # Annual interest rate (8%)
time_in_years = 6  # Time in years
compounds_per_year = 10  # Number of times interest is compounded per year

interest_earned = calculate_compound_interest(principal, annual_rate, time_in_years, compounds_per_year)
print("Compound interest earned: $", round(interest_earned, 2))

# Assignment 2: Create a script that displays the current time and updates every second.
import datetime
import time

def show_current_time():
    try:
        while True:
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            print("Current Time:", current_time)
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nTime display stopped.")

# Start showing the time
show_current_time()

# Congratulations on completing the in-depth section on Python's math and datetime modules!
# Review the assignments, try to solve them, and check your understanding of these powerful tools.

