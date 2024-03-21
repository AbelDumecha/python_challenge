import os
import csv
# select path to collect CSV data 
budget_data = os.path.join("..", "Resources", "budget_data.csv")

#Read the CSV file and iterate through each row
with open(budget_data) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter= ",")
    #store the header row
    header_row = next(csv_reader) 
    # define variables
    total_months = 0 
    net_total = 0
    changes = []
    dates =[]
    #calculate total months, net total amount, changes, and dates
    previous_value = None
    for row in csv_reader:
        total_months += 1
        value = int(row[1])
        net_total += value
        if previous_value is not None:
            change = value - previous_value
            changes.append(change)
            dates.append(row[0])
        previous_value = value
#calculate average change
if changes:
    total_change = sum(changes)
    num_changes = len(changes)
    average_change = total_change / num_changes
else:
    average_change = 0
    
#Find greatest increase and decrease in profits
if changes: 
    greatest_increase = int(max(changes))
    greatest_decrease = int(min(changes))
    increase_index = changes.index(greatest_increase)
    decrease_index = changes.index(greatest_decrease)
    greatest_increase_date = dates[increase_index]
    greatest_decrease_date = dates[decrease_index]
else:
    greatest_increase = 0
    greatest_decrease = 0
    greatest_increase_date = "N/A"
    greatest_decrease_date = "N/A"

#print the analysis 
print("Financial Analysis")
print("-----------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")   
print(f"Average Change: ${average_change: .2f}")
print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})") 

# Define Txt. folder path 
output_folder = os.path.join(os.getcwd(), "Analysis")

# Define Txt path within the output folder
output_file = os.path.join(output_folder, "analysis_results.txt")

# Write the analysis to the output file
with open(output_file, 'w') as txt_file:
    txt_file.write("Financial Analysis\n")
    txt_file.write("-----------\n")
    txt_file.write(f"Total Months: {total_months}\n")
    txt_file.write(f"Total: ${net_total}\n")
    txt_file.write(f"Average Change: ${average_change:.2f}\n")
    txt_file.write(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})\n")
    txt_file.write(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})\n")

print(f"Analysis written to {output_file}")