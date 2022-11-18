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

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    # Print the header row.
    headers = next(file_reader)
    print(headers)

    # Print each row in the CSV file.
    #for row in file_reader:
       # print(row)

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
