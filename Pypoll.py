#Pypoll

#The data we need to retrieve.
import csv

import os

#Resources/election_results.csv
# Assign a variable for the file to load and the path.
#file_to_load = 'Resources/election_results.csv'
file_to_load = os.path.join("Resources", "election_results.csv")

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

#1. the total number of votes cast
total_votes = 0

#add candidate option variable
candidate_options = []

#create voter dictionary
candidate_votes = {}

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

        # Determine the percentage of votes for each candidate by looping through the counts.
        # 1. Iterate through the candidate list.
    for candidate_name in candidate_votes:

        #vote count
        votes = candidate_votes[candidate_name]

        #calculate percentage
        #vote_percentage = float(votes) / float(total_votes) * 100

        #print candidadate name and percentage
        print(f"{candidate_name}: received {votes / total_votes * 100:.2f}% of the vote.")


    #print(total_votes)
#print(candidate_options)
print(candidate_votes)

    

    # To do: perform analysis.
    #print(election_data)

# Close the file.
election_data.close()



# Using the open() function with the "w" mode we will write data to the file.
#outfile = open(file_to_save, "w")
# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:

# Write some data to the file.
#outfile.write("Hello World")
    txt_file.write("Counties in the Election\n-------------------\n")
    txt_file.write("Arapahoe\nDenver\nJefferson")

# Close the file
#outfile.close()
txt_file.close()


#1. the total number of votes cast
#2. A complete list of candidates who received votes
#3. The percentage of votes each candidtae won
#4. The total number of votes each candidate won
#5. The winner of the election based on popular vote
