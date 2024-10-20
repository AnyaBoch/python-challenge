# python-challenge
Module 3 home assignment for PyBank and PyPoll

**1 - PyBank **
**_Instructions_**
In this Challenge, I am tasked with creating a Python script to analyze the financial records of some company. I was given a financial dataset called budget_data.csv. The dataset is composed of two columns: "Date" and "Profit/Losses".
My task was to create a Python script that analyzes the records to calculate each of the following values:
- The total number of months included in the dataset
- The net total amount of "Profit/Losses" over the entire period
- The changes in "Profit/Losses" over the entire period, and then the average of those changes
- The greatest increase in profits (date and amount) over the entire period
- The greatest decrease in profits (date and amount) over the entire period

My analysis should be aligned with the following results:
**Financial Analysis**
Total Months: 86
Total: $22564198
Average Change: $-8311.11
Greatest Increase in Profits: Aug-16 ($1862002)
Greatest Decrease in Profits: Feb-14 ($-1825558)
In addition, my final script should both print the analysis to the terminal and export a text file with the results.

**_PyBank difficulties:_**
I struggles a lot for this assignment. I needed help of a tutor cause I neede more explanation for calculations, sequence, and coding methods. The tutor provided the work as a sample. My problem was easily solved in Excel, but here it turned out to be quite a challenging task. I was working on PyBank using conditions such as: 
**if previous_value is not None**: and **if previous_profit != ""**, which ChatGPT suggested. However, the code only worked when the conditions started as **if total_months > 1**."link for this work: https://pastebin.com/cKGk0UZd


**2 - PyPoll**
**_Instructions:_**
In this Challenge, I am tasked with helping a small, rural town modernize its vote-counting process.

I was given a set of poll data called election_data.csv. The dataset is composed of three columns: "Voter ID", "County", and "Candidate". My task was to create a Python script that analyzes the votes and calculates each of the following values:

-The total number of votes cast
-A complete list of candidates who received votes
-The percentage of votes each candidate won
-The total number of votes each candidate won
-The winner of the election based on popular vote
-In addition, my final script should both print the analysis to the terminal and export a text file with the results.


**Election Results**
Total Votes: 369711
Charles Casper Stockham: 23.049% (85213)
Diana DeGette: 73.812% (272892)
Raymon Anthony Doane: 3.139% (11606)
Winner: Diana DeGette
In addition, my final script should has both print the analysis to the terminal and export a text file with the results. Same like previous assignment.


**_PyPoll difficulties:_**
I went the easier way creatring biblioteque of candidates, and it works perfectly fine. Chat GPT and Xpert Learning assistant rock.
