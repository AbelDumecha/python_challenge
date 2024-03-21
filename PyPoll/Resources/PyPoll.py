import os
import csv
# select path to collect CSV data 
election = os.path.join("..", "Resources", "election_data.csv")

#Read the CSV file and iterate through each row
with open(election) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter= ",")
    #store the header row
    header_row = next(csv_reader) 
    # define variables
    total_votes = 0
    candidates_votes = {}
    winner = ""
    max_votes = 0
    #calculate the total_vote, candidates vote,  and the winner
    for row in csv_reader:
        total_votes += 1
        candidate = row[2]
        
        #increment candidates' count if available in the data set 
        if candidate in candidates_votes:
            candidates_votes[candidate] += 1
       #if candidate is not in the data set, add them with 1 vote
        else: 
            candidates_votes[candidate] = 1

#Calculate each candidates' result in percent
candidates_percentages = {}
for candidate, votes in candidates_votes.items():
    percentage = (votes / total_votes) * 100
    candidates_percentages[candidate] = percentage

#Declaring the winner
for candidate, votes in candidates_votes.items():
    if votes > max_votes:
        max_votes = votes
        winner = candidate

#print anaylsis
print("Election Results")
print("--------------") 
print(f"Total votes: {total_votes}")
print("--------------------------")
for candidate, votes in candidates_votes.items():
    print(f"{candidate}: {candidates_percentages[candidate]: .3f}% ({votes})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")   

# Export the analysis results to a text file
# Define Txt. folder path 
output_folder = os.path.join(os.getcwd(), "Analysis")
# Define Txt path within the output folder
output_file = os.path.join(output_folder, "analysis_results.txt")
with open(output_file, 'w') as txtfile:
    txtfile.write("Election Results\n")
    txtfile.write("-------------------------\n")
    txtfile.write(f"Total Votes: {total_votes}\n")
    txtfile.write("-------------------------\n")
    for candidate, votes in candidates_votes.items():
        txtfile.write(f"{candidate}: {candidates_percentages[candidate]:.3f}% ({votes})\n")
    txtfile.write("-------------------------\n")
    txtfile.write(f"Winner: {winner}\n")
    txtfile.write("-------------------------\n")

print(f"Analysis results exported to {output_file}")