# PART 1 - Reading that cvs file 

# import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

#Read the csv file

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is no header)

    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

# PART 2 - Processing the Data.

# Initialise variables

total_months = 0  # Total Months
total_profit = 0
previous_profit = 0
ave_change = 0
max_increase = 0
max_decrease = 0
max_increase_month = ""
max_decrease_month = ""

changes = []

with open(csvpath, mode='r') as csvfile:
    csv_reader = csv.reader(csvfile)
    
    # Skip the header row
    next(csv_reader, None)

    for row in csv_reader:
        # Calculate total profit
        total_profit += int(row[1])
        
        # Calculate monthly change and store it in the 'changes' list
        if total_months > 0:
            monthly_change = int(row[1]) - previous_profit
            changes.append(monthly_change)
        
        # Check for greatest increase and decrease
            if monthly_change > max_increase:
                max_increase = monthly_change
                max_increase_month = row[0]
            elif monthly_change < max_decrease:
                max_decrease = monthly_change
                max_decrease_month = row[0]
                
        # Update previous profit for the next iteration
        previous_profit = int(row[1])
        
        total_months += 1

# Calculate the average change
average_change = sum(changes) / len(changes)

# Define the path for the output text file
# output_file = os.path.join('Output', 'financial_analysis.txt')

# Open the file for writing
with open('financial_analysis.txt', 'w') as file:

    # Write the results to the text file
    file.write("----------------------------------------")
    file.write("Financial Analysis\n")
    file.write("----------------------------------------\n")
    file.write("Total Months: " + str(total_months) + "\n")
    file.write("Total Profit: " + str(total_profit) + "\n")
    file.write("Average Change: " + str(round(average_change, 2)) + "\n")
    file.write("Greatest Increase in Profits: " + max_increase_month + " (" + str(max_increase) + ")\n")
    file.write("Greatest Decrease in Profits: " + max_decrease_month + " (" + str(max_decrease) + ")\n")
    file.write("----------------------------------------")
# Print the results to the terminal

print("----------------------------------------")
print("Financial Analysis")
print("----------------------------------------")
print("Total Months:", total_months)
print("Total Profit:", total_profit)
print("Average Change:", round(average_change, 2))
print("Greatest Increase in Profits:", max_increase_month, "(", max_increase, ")")
print("Greatest Decrease in Profits:", max_decrease_month, "(", max_decrease, ")")
print("----------------------------------------")
print()
# Inform the user about the file creation
print("Results have been saved to 'financial_analysis.txt'")
