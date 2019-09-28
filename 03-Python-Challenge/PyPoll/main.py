import os
import csv


csvpath = os.path.join('..','Resources', 'election_data.csv')
wordpath = os.path.join('..', 'Analysis', 'election_analysis.txt')

with open(csvpath, newline='') as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=',')

    next(csvreader) 


    total_vote = 0
    candidate = ""
    vote_data = {}
    candidate_list = []
    voteID = []
    percentage_vote = []
    winner_list = []
    winner = ""

    for row in csvreader:
        total_vote +=1
        candidate = row[2]
        
        if candidate in vote_data.keys():
            vote_data[candidate] = vote_data[candidate] + 1
        else:
            vote_data[candidate] = 1 

for key, value in vote_data.items():
    candidate_list.append(key)
    voteID.append(value)

for vote in voteID:
    percentage_vote.append(round(vote/total_vote * 100))

vote_data_updated = list(zip(candidate_list, percentage_vote, voteID))

election_data = (f"{candidate_list}:\n{percentage_vote}%:\n{voteID}\n")
    # Don't know how to extract elements from candidate_list, percentage_vote, and voteID to put them side by side

for person in vote_data_updated:
    if max(percentage_vote) == person[1]:
        winner = person[0]
    
election_summary = (
f"-------------------------\n"
f"Total Vote: {total_vote}\n"
f"-------------------------\n"
f"The election results are:\n"
f"{election_data}"
f"-------------------------\n"
f"The Winner is {winner}\n")

print(election_summary, end="")


with open(wordpath, "w") as txt_file:
    txt_file.write(election_summary)