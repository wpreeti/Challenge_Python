import os
import csv
from pathlib import Path

# Create lists for Election Result
Votelist=[]
totalvotes = 0 

# Create list of variables for unique candidates
Candidates=[]
Candidatevotecount=[]
Candidatevotepct=[]

# Set path for the file
election_data = os.path.join(Path.home(),"Bootcamp-Homework/Challenge_Python/PyPoll/Resources","election_data.csv")
output_file = os.path.join(Path.home(),"Bootcamp-Homework/Challenge_Python/PyPoll/Analysis","PyPoll.txt")

# Read csv
with open(election_data) as csvfile:
    csvreader=csv.reader(csvfile, delimiter =',')
    header=next(csvreader)
    for row in csvreader:
        Votelist.append(row[2])

totalvotes = len(Votelist)

# Print Total votes in Election Results
print("Election Results")
print("--------------------------")
print(f"Total Votes: {totalvotes}")
print("--------------------------")


# Assign indexes to all candidates
for name in Votelist:
    if name not in Candidates:
        Candidates.append(name)
        
lastCandidateVotes = 0

for candidate in Candidates:
    currentCandidateVotes = 0
    
    for vote in Votelist:
        if candidate == vote:
            currentCandidateVotes +=1
    percent = currentCandidateVotes/ len(Votelist)
    Candidatevotecount.append(currentCandidateVotes)
    Candidatevotepct.append(percent)
    
    if lastCandidateVotes < currentCandidateVotes:
        Winner = candidate
        lastCandidateVotes = currentCandidateVotes

    print(f"{candidate}: {percent:.3%} ({currentCandidateVotes})")

print("---------------------------")
print(f"Winner: {Winner}")
print("---------------------------")

# Output to text file 

with open(output_file, 'w') as output:
    output.write("Election Results\n")
    output.write("-"*50+"\n")
    output.write(f"Total Votes: {totalvotes}\n")
    output.write("-"*50+"\n")
    for candidate in Candidates:
        index = Candidates.index(candidate)
        output.write(f"{candidate}: {Candidatevotepct[index]:.3%} ({Candidatevotecount[index]})\n")
    output.write("-"*50+"\n")
    output.write(f"Winner: {Winner}\n")
    output.write("-"*50+"\n")
    
    

    






    
