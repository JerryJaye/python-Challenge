
Python CHALLENGE

Project - PyBank - Analysis of monthly Profit and Loss Data.

I separated the code development of this project into 3 parts. Part 1 was reading the CSV file, budgdet_data.csv, into the program. I imported the os module to allow the creation of file paths across operating systems, and then the csv module for reading of the budget_data.csv file.

I confirmed that the read was successful by printing the csv header, that was now stored as csv_header.

PART 2 of the code is processing the data and preparing it for output. This involved selecting and initialising the variables needed from processing to calculate the items required. Data are processed in a combination of For loops and nested if elif statements. The differences between the P & L results each month were calculated and appended to a new list. I used the content of this List to calculate the average (mean) change over the 86 months., and that Greatest Increase and Greatest Decrease in the changes in Monthly P&L. 

PART 3 is the outputting of results to both a text file and to the Terminal. I out to a text file, financial_analysis.txt first, and then to the terminal. I thought I would be a bit cheeky and print out both the month and amount of these values. The text file is in both the PyBank folder, and the PyBank\analysis folder.

ICode file = Mainbank.py
Input file = budget_data.csv
Output file = financial_analysis.txt

Project - PyPoll - Vote Counting and Reporting the Winner.

As with the PyBank project the code development for this project was in 3 Parts. Part 1 was reading the CVS file, election_data.csv, into the program. The code is almost identical to the PyBank project. Again, I confirmed that the read was successful by printing the csv header, that was now stored as csv_header.

PART 2 - Processing of the Data. The data were processed using a For loop to count the votes for each of the three candidates. How ever, unlike in the PyBank Project, the processing and generation of results continued in the Part 3 - the output section of the code. Of the processing was a For loop that would output, the names of the three candidates, together with the number of votes each had, the percentage of the votes in each case. So it was more than and simple write each line to a text file. I thought it would be interesting to see if I could write out to a text file while also writing to a text file. This proved to be more complicated. I received some help from ChatGDP in coding and debugging this code.

Code file = Mainpol.py
Input file = election_data.csv
Output file = election_results.txt

I have I have used resources from Eric Matthes book, Python Crash Course, and some interaction from ChatGDP in preparing this python-Challenge.





