"""
Author: Lutz, Melissa
Date: 09/11/2025
File Name: Lutz_lemonadeStandSchedule.py
Description: Program to manage a weekly lemonade stand schedule using lists, loops, and conditionals.
"""

# List of tasks related to running the lemonade stand
tasks = [
    "Buy lemons",
    "Make lemonade",
    "Sell lemonade",
    "Count earnings",
    "Clean up"
]

# Print out the list of tasks
print("-- TASK LIST --")
for task in tasks:   # loop through each task
    print(task)

print("\n")  # blank line for readability

# List of days in the week
days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

# Assign tasks to days with conditionals
print("-- WEEKLY SCHEDULE --")
for i, day in enumerate(days):
    if day == "Saturday" or day == "Sunday":
        # Weekend rest days
        print(f"{day}: Day off! Time to rest and recharge.")
    else:
        # Weekdays get tasks assigned in order
        task = tasks[i % len(tasks)]
        print(f"{day}: {task}")
