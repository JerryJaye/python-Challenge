#PART 1 - Import the CSV data file.

# Import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

csvpath = os.path.join('Resources', 'election_data.csv')

#Read the csv file

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is no header)

    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

# PART 2 - Processing the data    

# Initialize a dictionary to store the vote counts for each candidate

candidate_votes = {}

# Initialize variable to store the total votes

total_votes = 0

# Open the CSV file.
   
with open(csvpath, mode = 'r') as csvfile:
 
    csv_reader = csv.reader(csvfile)
    
    # Skip the header row
    next(csv_reader, None)
    
    # Iterate through the rows in the CSV file
    for row in csv_reader:
        # Assuming Candidate names are in column 2 (index 1)
        candidate = row[2]
        
        # Check if the candidate is already in the dictionary, and if not, initialize their count to 0
        if candidate not in candidate_votes:
            candidate_votes[candidate] = 0
        
        # Increment the vote count for the candidate
        candidate_votes[candidate] += 1
        
        # Increment the total votes
        total_votes += 1

# PART 3 - Output results - Write to a Text File and to the Terminal

# The secion below outputs to both a text file named election-results.text and to the Terminal.
# Open a file for writing (or create it if it doesn't exist)
with open('election_results.txt', 'w') as file:
    # Print the header to both the terminal and the file
    header = (
        "\nElection Results\n"
        "---------------------------------------\n\n"
        f'Total Votes: {total_votes}\n\n'
        "----------------------------------------\n\n"
    )
    print(header)
    file.write(header)

    # Print the results for each candidate to both terminal and file
    for candidate, votes in candidate_votes.items():
        # Calculate the percentage votes for each candidate
        numvotes = int(votes)
        percentvotes = round(numvotes / total_votes * 100, 3)

        result_line = f'{candidate}:   {percentvotes}%    {votes} votes'
        print(result_line)  # Print to terminal
        file.write(result_line + '\n')  # Write to file

    # Dashed line after the results in both terminal and file
    dash_line = "\n----------------------------------------\n"
    print(dash_line)  # Print to terminal
    file.write(dash_line)  # Write to file

    # Find the winner (candidate with the most votes)
    winner = max(candidate_votes, key=candidate_votes.get)
    winner_line = f'\nThe winner is {winner} with {candidate_votes[winner]} votes.\n'
    print(winner_line)  # Print to terminal
    file.write(winner_line)  # Write to file

    # Dashed line after the winner in both terminal and file
    print(dash_line)  # Print to terminal
    file.write(dash_line)  # Write to file

print("Results have been written to 'election_results.txt'")