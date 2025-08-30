"""
Author: Melissa Lutz
Date: 8/30/2025
File Name: Lutz_lemonadeStand.py
Description: A simple program that simulates a lemonade stand using functions to calculate cost and profit.
"""

# Function to calculate the total cost of making lemonade
def calculate_cost(lemons_cost, sugar_cost):
    # Adding the cost of lemons and sugar
    total_cost = lemons_cost + sugar_cost
    return total_cost  # Returning the total cost

# Function to calculate the profit from selling lemonade
def calculate_profit(lemons_cost, sugar_cost, selling_price):
    # Profit is the selling price minus the cost
    profit = selling_price - (lemons_cost + sugar_cost)
    return profit  # Returning the profit

# ---------------- Test Variables ----------------
lemons_cost = 4.50   # Example cost of lemons
sugar_cost = 2.75    # Example cost of sugar
selling_price = 12.00  # Example selling price of lemonade

# ---------------- Calling Functions ----------------
# Build result string for cost
cost_result = f"{lemons_cost} + {sugar_cost} = {calculate_cost(lemons_cost, sugar_cost)}"

# Get profit calculation
profit_result = calculate_profit(lemons_cost, sugar_cost, selling_price)

# ---------------- Console Output ----------------
print("Lemonade Stand Simulation")
print("--------------------------")
print("Cost Calculation:")
print("Cost Formula = " + cost_result)
print("Profit Calculation:")
print("Profit = $" + str(profit_result))
