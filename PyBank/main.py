# Dependencies
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "budget_data.csv")  # Input file path
file_to_output = os.path.join("Analysis", "PyBank_analysis.txt")  # Output file path

# Variable to count the total months
total_months = 0  # Starting the count at zero
total_net = 0 #Create a variable for total net 
profit_losses = []  # New list to collect all profit/loss values
dates = []  # List to collect dates

# Open the CSV file and print its content
with open(file_to_load, encoding='UTF-8') as csvfile:
    reader = csv.reader(csvfile)  # Create the CSV reader object
    header = next(reader)  # Skip the header row
    print(f"Header: {header}")  # Print the header to verify it was skipped

# Loop through each row and count the months
    for row in reader:
        total_months = total_months + 1  # Adding 1 for each row (month)
        profit_loss = int(row[1])  # Access Col1 and convert the value to an integer
        total_net = total_net + profit_loss #sum the value of where the loop is plus the next one
        profit_losses.append(profit_loss)  # Store each profit/loss value
        dates.append(row[0])  # Store date from Col0

# Now calculate net change after collecting all values
net_changes = []  # List for storing monthly differences

for i in range(1, len(profit_losses)):  # Start from second month
    net_change = profit_losses[i] - profit_losses[i - 1]  # Current minus Previous
    net_changes.append(net_change) #add the monthly difference number to this list


total_net_change = sum(net_changes)  # Add up all the monthly net changes

# Calculate the average net change
average_net_change = total_net_change / len(net_changes)  # Divide by number of changes

# Calculate the greatest increase and decrease in profits
greatest_increase = max(net_changes)  # Find the largest positive change
greatest_decrease = min(net_changes)  # Find the largest negative change

# Find the index of these changes in the net_changes list
greatest_increase_index = net_changes.index(greatest_increase)
greatest_decrease_index = net_changes.index(greatest_decrease)

# Use the `dates` list for correct month references
greatest_increase_month = dates[greatest_increase_index + 1]  
greatest_decrease_month = dates[greatest_decrease_index + 1]  

# Print the result
print(f"Total Months: {total_months}")
print(f"Total Net: ${total_net}")
print(f"Average Net Change: ${average_net_change:.2f}")  # Rounded for clarity
print(f"Greatest Increase in Profits: ${greatest_increase} in {greatest_increase_month}")
print(f"Greatest Decrease in Profits: ${greatest_decrease} in {greatest_decrease_month}")


# Write the Results to a Text File
with open(file_to_output, "w") as txt_file:
    txt_file.write(f"Total Months: {total_months}\n")
    txt_file.write(f"Total Net: ${total_net}\n")
    txt_file.write(f"Average Net Change: ${average_net_change:.2f}\n")
    txt_file.write(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})\n")
    txt_file.write(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})\n")