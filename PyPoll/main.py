import os
import csv
from pathlib import Path 

cwd = os.getcwd()
csvpath = os.path.join("Resources", "election_data.csv")
totalvotes = 0
khan_votes = 0
correy_votes = 0
li_votes = 0
tooley_votes = 0
votes = 0


with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    csvheader = next(csvreader)
    for row in csvreader:
        voter_id = row[0]
        county = row[1]
        candidate = row[2]
        # Totaling the votes cast
        totalvotes = totalvotes + 1
        # Totaling the votecount by each candidates
        if candidate == "Khan":
            khan_votes = khan_votes + 1
        if candidate == "Correy":
            correy_votes = correy_votes + 1
        if candidate == "Li":
            li_votes = li_votes + 1
        if candidate == "O'Tooley":
            tooley_votes = tooley_votes + 1

        
        #Listing all the votes that matches with each candidates
        candidates = {
            "Khan": khan_votes, 
            "Correy": correy_votes,
            "Li": li_votes, 
            "O'Tooley": tooley_votes
        }
        # Printing the dictionay
        # print(candidates)
        # Finding winner
        for candidate, value in candidates.items():
            if value > votes:
                votes = value 
                winner = candidate

khan_percent = (khan_votes/totalvotes) *100
correy_percent = (correy_votes/totalvotes) * 100
li_percent = (li_votes/totalvotes)* 100
tooley_percent = (tooley_votes/totalvotes) * 100


def Result():
    print("\tElection Results\n")
    print("\t------------------")
    print(f'Total Votes: {totalvotes}\n')
    print("--------------\n")
    print(f'Khan: {khan_percent: .3f}% ({khan_votes})')
    print(f'Correy: {correy_percent: .3f}% ({correy_votes})')
    print(f'Li: {li_percent: .3f}% ({li_votes})')
    print(f"O'Tooley: {tooley_percent: .3f}% ({tooley_votes})")

    print(f'Winner: {winner}')
Result()

output = open("PyPoll_Summary.txt", "w")
output.write("\tElection Results\n")
output.write("--------------------------\n")
output.write(f"Total Votes: {totalvotes}\n")
output.write("--------------------------\n")
output.write(f'Khan: {khan_percent: .3f}% ({khan_votes})\n')
output.write(f'Correy: {correy_percent: .3f}% ({correy_votes})\n')
output.write(f'Li: {li_percent: .3f}% ({li_votes})\n')
output.write(f"O'Tooley: {tooley_percent: .3f}% ({tooley_votes})\n")

output.write(f'Winner: {winner}')
