#Modules 

import os
import csv
from enum import unique
from nbformat import write

#create variables 
candidates = []
candidates_diff = []
vote_count = []
vote_percentage = []
votes = 0.0

#reading the csv file 
csv_path = os.path.join('Resources', 'election_data.csv')

with open(csv_path) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')
    header = next(csv_reader) #saving header 

    for row in csv_reader:
        votes += 1
        candidates.append(row[2])

    for i in set(candidates):
        candidates_diff.append(i)

        # setting variable x equal to total votes 
        x = candidates.count(i)
        #saving to vote_count
        vote_count.append(x)
        #saving y as vote percent 
        y = (x/votes)
        #append to vote_percentage
        vote_percentage.append(y)

    winner_count = max(vote_count)
    winner = candidates_diff[vote_count.index(winner_count)]

print("Election Results")
print("-----------------")
print(f"Total Votes: {votes}")
print("------------------")
for z in range(len(set(candidates_diff))):
    print(f"{candidates_diff[z]} : {vote_percentage[z]}% ({vote_count})")
print(f"WINNER: {winner}")