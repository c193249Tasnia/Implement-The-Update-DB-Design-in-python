# Python File I/O and JSON Handling: Comprehensive Guide
tasnia sharmin
ID: C193249
Email: c193249@ugrad.iiuc.ac.bd
"""
# Section 1: Plain Text Files
# ---------------------------
# Reading and writing plain text files is often the first step in file manipulation.

# Section 2: CSV Files
# --------------------
# CSV (Comma-Separated Values) files are commonly used for storing tabular data.

# Section 4: Practical Applications
# ---------------------------------
# Combining file I/O with real-world data processing.

# Assignments
# -----------
# Assignment 1: Write a script that reads a CSV file containing product information and converts it into a JSON file.

import csv
import json

def convert_csv_to_json(input_csv, output_json):
    # List to store product information
    product_list = []
    
    # Open and read the CSV file
    with open(input_csv, mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        
        # Convert each row in CSV into a dictionary and add to the list
        for row in csv_reader:
            product_list.append(row)
    
    # Write the list to a JSON file
    with open(output_json, mode='w') as json_file:
        json.dump(product_list, json_file, indent=4)
    
    print(f"Successfully converted {input_csv} to {output_json}!")

# Creating a sample CSV file for demonstration
sample_csv = 'sample_products.csv'
sample_json = 'sample_products.json'

with open(sample_csv, mode='w', newline='') as csv_file:
    fieldnames = ["Product", "Price", "In_Stock"]
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    
    # Writing the header
    writer.writeheader()
    
    # Writing some product data
    writer.writerow({"Product": "Smartphone", "Price": 699, "In_Stock": "Yes"})
    writer.writerow({"Product": "Laptop", "Price": 999, "In_Stock": "No"})
    writer.writerow({"Product": "Tablet", "Price": 399, "In_Stock": "Yes"})

# Convert the sample CSV to JSON
convert_csv_to_json(sample_csv, sample_json)

# Assignment 2: Create a log file writer that appends log messages to a file with timestamps.

from datetime import datetime

def append_to_log(message, log_file):
    # Get the current time and format it
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Create a formatted log entry
    log_entry = f"[{current_time}] {message}\n"
    
    # Open the log file in append mode and write the log entry
    with open(log_file, mode='a') as file:
        file.write(log_entry)
    
    print(f"Log entry added: {message}")

# Example usage:
log_file = 'activity_log.txt'
append_to_log("Application started", log_file)
append_to_log("User logged in", log_file)
append_to_log("Error: Unable to connect to database", log_file)

print(f"Log entries have been written to {log_file}")

# Congratulations on completing the comprehensive section on Python file I/O and JSON handling!
# Review the assignments, try to solve them, and check your understanding of file operations and data formats.
