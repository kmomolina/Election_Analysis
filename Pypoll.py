#Pypoll

#The data we need to retrieve.
import csv

import os

#Resources/election_results.csv
# Assign a variable for the file to load and the path.
#file_to_load = 'Resources/election_results.csv'
file_to_load = os.path.join("Resources", "election_results.csv")

# Create a filename variable to save direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

#1. the total number of votes cast
total_votes = 0

#add candidate option variable
candidate_options = []

#create voter dictionary
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)
    #print(headers)

    # Print each row in the CSV file.
    for row in file_reader:

        #add the total vote count
        total_votes += 1

        # Print the candidate name from each row
        candidate_name = row[2]

        #If the candidate does not match existing name
        if candidate_name not in candidate_options:

            #add the candidate name to the candidate list
            candidate_options.append(candidate_name)

            #start tracking cadidate vote count
            candidate_votes[candidate_name] = 0

        #add votes to the candidates count
        candidate_votes[candidate_name] += 1

#save results to text file
with open(file_to_save, "w") as txt_file:

    # Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    # Save the final vote count to the text file.
    txt_file.write(election_results)
    #txt_file.write("Election Results\n-------------------\n")
    #txt_file.write(f"Total Votes: {total_votes}\n------------------------\n")

        # Determine the percentage of votes for each candidate by looping through the counts.
        # 1. Iterate through the candidate list.
    for candidate_name in candidate_votes:

        #vote count
        votes = candidate_votes[candidate_name]
        #calculate percentage
        vote_percentage = float(votes) / float(total_votes) * 100

    #print out each candidate's name, vote count, and percentage of votes to the terminal.
    #print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

    # Print each candidate, their voter count, and percentage to the terminal.
        print(candidate_results)
    #  Save the candidate results to our text file.
        txt_file.write(candidate_results)

        # Determine winning vote count and candidate
        # 1. Determine if the votes are greater than the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
                # 2. If true then set winning_count = votes and winning_percent =
                # vote_percentage.
            winning_count = votes
            winning_percentage = vote_percentage
                # 3. Set the winning_candidate equal to the candidate's name.
            winning_candidate = candidate_name

    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    txt_file.write(winning_candidate_summary)

        #print candidadate name and percentage
        #print(f"{candidate_name}: received {votes / total_votes * 100:.2f}% of the vote.")

#  To do: print out the winning candidate, vote count and percentage to terminal.

    #print(total_votes)
#print(candidate_options)
#print(candidate_votes)

    

    # To do: perform analysis.
    #print(election_data)

# Close the file.
election_data.close()



# Using the open() function with the "w" mode we will write data to the file.
#outfile = open(file_to_save, "w")
# Using the with statement open the file as a text file.
#with open(file_to_save, "w") as txt_file:

# Write some data to the file.
#outfile.write("Hello World")
    #txt_file.write("Counties in the Election\n-------------------\n")
    #txt_file.write("Arapahoe\nDenver\nJefferson")

# Close the file
#outfile.close()
txt_file.close()


#1. the total number of votes cast
#2. A complete list of candidates who received votes
#3. The percentage of votes each candidtae won
#4. The total number of votes each candidate won
#5. The winner of the election based on popular vote
