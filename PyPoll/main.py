#Name: Dinnara Hitt
#Python-Chalenge
#PyPoll 

import os
import csv

csvpath = os.path.join ('Resources', 'PyPoll_Resources_election_data.csv')
output_path = os.path.join ("Resources", "output_election_data.txt")

total_votes = 0
total_Khan = 0
total_Correy = 0
total_Li = 0
total_Tooley = 0
total_none = 0

list_candidates = ['Khan','Correy','Li',"O'Tooley"]
list_total_votes = []

winner_total = 0
winner_index = 0
winner_name = ""

percent_Khan = 0.000
percent_Correy = 0.000
percent_Li = 0.000
percent_Tooley = 0.000

with open(csvpath) as csvfile:
	
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first 
    csv_header = next(csvreader)
    
    # for loop to read each row of data after the header 
    # count votes for each candidate
    
    for row in csvreader:
    	
    	total_votes += 1
    	
    	if row[2] == "Khan" :
    		total_Khan += 1 
    	elif row[2] == "Correy" :
    		total_Correy += 1
    	elif row[2] == "Li" :
    		total_Li += 1
    	elif row[2] == "O'Tooley" :
    		total_Tooley += 1
    	else:
    		total_none += 1

#Calculates percentage of each candidate
percent_Khan = float((total_Khan * 100) / total_votes)
percent_Correy =  float((total_Correy * 100) / total_votes)
percent_Li =  float((total_Li * 100) / total_votes)
percent_Tooley =  float((total_Tooley * 100) / total_votes)

#Insert candidates votes in list_total_votes to retrieve the winner
list_total_votes.insert(0,total_Khan)
list_total_votes.insert(1,total_Correy)
list_total_votes.insert(2,total_Li)
list_total_votes.insert(3,total_Tooley)

#Find the max of votes and the name winner name(with the max index)
winner_total = max(list_total_votes)
winner_index = list_total_votes.index(winner_total)
winner_name = list_candidates[winner_index]

#Print Output
print ('Election Results')
print ('-----------------------------')
print (f'Total votes: {total_votes}')
print ('-----------------------------')
print (f'Khan: {round(percent_Khan,3)}% ({total_Khan})')
print (f'Correy: {round(percent_Correy,3)}% ({total_Correy})')
print (f'Li: {round(percent_Li,3)}% ({total_Li})')
print (f"O'Tooley: {round(percent_Tooley,3)}% ({total_Tooley})")
print ('-----------------------------')
print (f"Winner: {winner_name}")
print ('-----------------------------')

#Write output in a text file
with open(output_path, 'w') as text_file:

    text_file.write('Election Results' + '\n')
    text_file.write('-----------------------------' + '\n')
    print (f'Total votes: {total_votes}', file=text_file)
    print ('-----------------------------', file=text_file)
    print (f'Khan: {round(percent_Khan,3)}% ({total_Khan})', file=text_file)
    print (f'Correy: {round(percent_Correy,3)}% ({total_Correy})', file=text_file)
    print (f'Li: {round(percent_Li,3)}% ({total_Li})', file=text_file)
    print (f"O'Tooley: {round(percent_Tooley,3)}% ({total_Tooley})", file=text_file)
    print ('-----------------------------', file=text_file)
    print (f"Winner: {winner_name}", file=text_file)
    print ('-----------------------------', file=text_file)



