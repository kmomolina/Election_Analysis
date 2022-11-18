print("hello world")
num_candidates = 3
winning_percentage = 73.81
candidate = "Diane"
won_election = True
counties = ["Arapahoe", "Denver", "Jefferson"]
if counties[1] == 'Denver':
    print(counties[1])

counties_dict = {"County": ["Arapahoe", "Denver", "Jefferson"]}

voting_data = []            
voting_data.append({"county": "Arapahoe", "registered_voters": 422829})
voting_data.append({"county": "Denver", "registered_voters": 463353})
voting_data.append({"county": "Jefferson", "registered_voters": 432438})

if "Arapahoe" in counties and "El Paso" in counties:
    print("Arapahoe and El Paso are in the list of counties.")
else:
    print("Arapahoe or El Paso is not in the list of counties.")

if "Arapahoe" in counties or "El Paso" in counties:
    print("Arapahoe or El Paso is in the list of counties.")
else:
    print("Arapahoe and El Paso are not in the list of counties.")

#print(counties_dict)
#print(voting_data)

for county in counties:
    print(county)

for county in counties_dict:
    print(county)

for county in counties_dict:
    print(counties_dict[county])

for county_dict in voting_data:
    print(county_dict)

for county, voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters.")


# How many votes did you get?

my_votes = int(input("How many votes did you get in the election? "))
#  Total votes in the election
total_votes = int(input("What is the total votes in the election? "))
# Calculate the percentage of votes you received.
#print(f"I received {my_votes/ total_votes* 100}% of the total votes.")

message_to_candidate = (
    f"You received {my_votes} number of votes. "
    f"The total number of votes in the election was {total_votes}. "
    f"You received {my_votes / total_votes * 100:.2f}% of the total votes.")

print(message_to_candidate)


# Import the DATETIME class from the datetime module.
import datetime as dt
# Use the now() attribute on the datetime class to get the present time.
now = dt.datetime.now()
# Print the present time.
print("The time right now is ", now)