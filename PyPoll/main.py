#import modules
import os
import csv

#set path for file
pypoll_csv = os.path.join('.','election_data.csv')

#set initial values and list
votes = 0
dict = {}

#open the csv to read
with open (pypoll_csv, newline='') as csvfile:
    
    #specify delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    
    #read the header row first  
    csv_header = next(csvreader)

    #create dictionary from file with unique candidates names as keys.
    for row in csvreader:
        #The total number of votes cast
        votes += 1
        #counts votes for each candidate as values
        #keeps a total vote count by counting up 1 for each row
        if row[2] in dict.keys():
            dict[row[2]] += 1
        else:
            dict[row[2]] = 1 

#create empty list for candidates and their votes count
candidates = []
cand_votes = []

#take dictionary keys and values and adds them to the lists
for key, value in dict.items():
    candidates.append(key)
    cand_votes.append(value)

#create percent list
percent = []

for i in cand_votes:
    percent.append(round(i/votes*100, 3))

#group candidates, cand_votes and percent into tuples
group = list(zip(candidates, cand_votes, percent))

#create winner list
winner_list= []

for candidate in group:
    if max(cand_votes) == candidate[1]:
       winner_list.append(candidate[0])

# makes winner_list a str with the first entry
winner = winner_list[0]

print("Election Results")
print("-------------------------")
#The total number of votes cast
print(f"Total Votes: {votes}")
print("-------------------------")
#A complete list of candidates who received votes
#The percentage of votes each candidate won
#The total number of votes each candidate won
for j in range(len(candidates)):
    print(candidates[j],": ",percent[j],"% (",cand_votes[j],")")
print("-------------------------")
#The winner of the election based on popular vote.
print("Winner: ",winner)
print("-------------------------")

#create text file in this path
text_file = os.path.join("Election Results.txt")

#write this in text 
with open("Election Results.txt", "w") as text_file:
    print("Election Results", file = text_file)
    print("-------------------------", file = text_file)
    print(f"Total Votes: {votes}", file = text_file)
    print("-------------------------", file = text_file)
    for j in range(len(candidates)):
        print(candidates[j],": ",percent[j],"% (",cand_votes[j],")", file = text_file)
    print("-------------------------", file = text_file)
    print("Winner: ",winner, file = text_file)
    print("-------------------------", file = text_file)