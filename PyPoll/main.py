# -*- coding: UTF-8 -*-
"""PyPoll Homework Starter File."""

# Import necessary modules
import csv
import os


# Files to load and output (update with correct file paths)
file_to_load = os.path.join('Resources/election_data.csv')  # Input file path
file_to_output = os.path.join('analysis/election_analysis.txt')  # Output file path


# Initialize variables to track the election data
total_votes = 0  # Track the total number of votes cast

# Define lists and dictionaries to track candidate names and vote counts
candidates = []

# Open the CSV file and process it
with open(file_to_load) as election_data:
    reader = csv.reader(election_data, delimiter=",")

    # Skip the header row
    header = next(reader)

    # Loop through each row of the dataset and process it
    for row in reader:
        #calculating all votes
        #total_votes += 1 #-same way as we did it into previous assignment PyBank but we shall do it in alternative way see ROW40
        # Creating candidates list:
        candidates.append(row[2])  # candidate names are in the third column
     
#Let's count votes now, but I am going to do it in other, simpler way for me, than it was offered in our assignment
#cause it is easier and works perfect
# Counting votes for each candidate:
charles_count = candidates.count("Charles Casper Stockham")
diana_count = candidates.count("Diana DeGette")
raymon_count = candidates.count("Raymon Anthony Doane")
##calculating all votes
total_votes = len(candidates) # another way of counting votes

# Calculating the percentage of votes each candidate received
charles_percentage = (charles_count / total_votes) * 100
diana_percentage = (diana_count / total_votes) * 100
raymon_percentage = (raymon_count / total_votes) * 100

# Determine the winner by comparing votes of three candidates:
if charles_count > diana_count and charles_count > raymon_count:
    winner = "Charles Casper Stockham"
elif diana_count > charles_count and diana_count > raymon_count:
    winner = "Diana DeGette"
else:
    winner = "Raymon Anthony Doane"

# Display the results
print(f"Total Votes: {total_votes}\n")
print(f"------------------------------")
print(f"Charles Casper Stockham: {charles_percentage:.2f}% (with {charles_count} votes)")
print(f"Diana DeGette: {diana_percentage:.2f}% (with {diana_count} votes)")
print(f"Raymon Anthony Doane: {raymon_percentage:.2f}% (with {raymon_count} votes)")
print(f"------------------------------")
print(f"THE WINNER IS: !!!!!!!{winner.upper()}!!!!!!!")
# Saving the winning candidate summary to the text file
#Printing the output
output = (
f"Election Results\n"
f"------------------------\n"
f"Total Votes: {total_votes}\n"
f"------------------------\n"
f"Charles Casper Stockham: {charles_percentage:.2f}% (with {charles_count} votes)\n"
f"Diana DeGette: {diana_percentage:.2f}% (with {diana_count} votes)\n"
f"Raymon Anthony Doane: {raymon_percentage:.2f}% (with {raymon_count} votes)\n" 
f"-------------------------\n"
f"THE WINNER IS: {winner.upper()}\n"
f"-------------------------\n"
)

with open(file_to_output, 'w') as txtfile:
    txtfile.write(output)

print(f"Output written to {file_to_output}")

# Election Results from assignment as an example what we should get in the end:
# Election Results
# -------------------------
# Total Votes: 369711
# -------------------------
# Charles Casper Stockham: 23.049% (85213)
# Diana DeGette: 73.812% (272892)
# Raymon Anthony Doane: 3.139% (11606)
# -------------------------
# Winner: Diana DeGette
# ------------------------