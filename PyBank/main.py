#-*- coding: UTF-8 -*-
"""PyBank Homework Starter File."""

# Dependencies
import csv
import os

# File path to the CSV file
file_to_load = os.path.join('Resources/budget_data.csv')  # input file path
file_to_output = os.path.join('Analysis/budget_analysis.txt')  # Output file path

# Initialize total sum variable
total_net = 0 
total_months = 0

# Add more variables to track other necessary financial data
changes_list = [] #we shall need the biblioteque for monthly changes
months_list = [] #and for months to count it properly 
previous_value = 0 


# Open and read the CSV file
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data, delimiter=",")
    header = next(reader)  # Read and skip the header row. #Extract first row to avoid appending to net_change_list
   #print(f"Header: {header}") #checking the step

    # Iterating through each row in the CSV
    for row in reader:
        # Track the total and net change of profit/loses
        total_net += int(row[1])  # Profit/Losses" column is the second column. found formula with chat gpt 
        # The total number of months included in the dataset
        total_months+= 1 # this is like total_months = total_months + 1 in VBA 
       
       #some more variables to find averages, min and max
        value = int(row[1])  ##reading cells' value in second column of the csv file
        date = row[0]  ##reading months and years in column 1
    
        if total_months > 1: ##so we skip not only the headers but first row where we cannot do some itterations
         change = value - previous_value #int(row[1]) - int(row-1[1])  
         changes_list.append(change) #creating list for changes
         months_list.append(row[0])  #creating list of dates
        
        previous_value  = value #updating previous value
        #    print(changes_list)

#calculating the average change in period of time :  
avg_change = round(sum(changes_list) / len(changes_list),2)
       
#calculating the greatest increase in profits (month and amount) and greatest decrease in losses (month and amount)
max_val = max(changes_list)
min_val = min (changes_list)

#and monthes and years that
max_month = months_list[changes_list.index(max_val)]
min_month = months_list[changes_list.index(min_val)]


# Print the output
print(f"Total: ${total_net}")
print(f"Total months: {total_months}")
#print(f"Total changes per  total months: {changes_list}")
print(f"Average change is: ${avg_change}")
print(f"Greatest Increase in Profits: {max_month}  (${max_val})")
print(f"Greatest Decrease in Profits: {min_month}  (${min_val})")


output = (
    f"Financial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_net}\n"
    f"Average Change: ${avg_change}\n"
    f"Greatest Increase in Profits: {max_month} (${max_val})\n"
    f"Greatest Decrease in Profits: {min_month} (${min_val})\n"
)

with open(file_to_output, 'w') as txtfile:
    txtfile.write(output)

print(f"Output written to {file_to_output}")


#comparing to results we got in assignment:
# Financial Analysis
# ----------------------------
# Total Months: 86
# Total: $22564198
# Average Change: $-8311.11
# Greatest Increase in Profits: Aug-16 ($1862002)
# Greatest Decrease in Profits: Feb-14 ($-1825558)