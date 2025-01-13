# Dependencies
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "election_data.csv")  # Input file path
file_to_output = os.path.join("Analysis", "PyPoll_analysis.txt")  # Output file path

# Variable to count the total number of votes
total_votes = 0  # Starting the count at zero

total_net = 0 #Create a variable for total net 
name_votes_dictionary = {}  # dictionary to collect all candidate names and votes

# Open the CSV file and print its content
with open(file_to_load, encoding='UTF-8') as csvfile:
    reader = csv.reader(csvfile)  # Create the CSV reader object
    header = next(reader)  # Skip the header row
    print(f"Header: {header}")  # Print the header to verify it was skipped

# Loop through each row and count the votes
    for row in reader:
        total_votes = total_votes + 1  # Adding 1 for each row (vote)
        candidate_name = row[2]  # Candidate is in the third column

        if candidate_name not in name_votes_dictionary:
            name_votes_dictionary[candidate_name] = 1  # Add a new candidate
        else:
            name_votes_dictionary[candidate_name] = name_votes_dictionary[candidate_name] +1  # Update an existing vote count
        

# Print the result
print(f"Total votes: {total_votes}")

# Loop through dictionary using .items() to print votes and percentages
for candidate_name, votes in name_votes_dictionary.items():
    percentage = (votes / total_votes) * 100
    print(f"{candidate_name}: {votes} votes ({percentage:.2f}%)")

highest_votes = 0
winner = ""

# Loop through dictionary using .items() to print the winner
for candidate_name, votes in name_votes_dictionary.items():
    if votes > highest_votes:  # Compare each candidate's votes
        highest_votes = votes  # Update highest vote count
        winner = candidate_name  # Update winner's name

print(f"Winner: {winner} with {highest_votes} votes!")

# Write the Results to a Text File
with open(file_to_output, "w") as txt_file:
    txt_file.write(f"Total votes: {total_votes}\n")
    txt_file.write(f"Winner: {winner} with {highest_votes} votes!\n")

# Loop through dictionary using .items() to print votes and percentages
    for candidate_name, votes in name_votes_dictionary.items():
        percentage = (votes / total_votes) * 100
        print(f"{candidate_name}: {votes} votes ({percentage:.2f}%)")
        txt_file.write(f"{candidate_name}: {votes} votes ({percentage:.2f}%)\n")

