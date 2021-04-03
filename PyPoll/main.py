'''
Name: Dinnara Hitt
Python-Chalenge
PyPoll 
'''
import os
import csv

csvpath = os.path.join ('Resources', 'election_data.csv')

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
winner_name = "Dinnara"

percent_Khan = 0.000
percent_Correy = 0.000
percent_Li = 0.000
percent_Tooley = 0.000

with open(csvpath) as csvfile:
	# CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    # Read each row of data after the header
    
    for row in csvreader:
    	#list_date.append(row[0])
    	#list_amount.append(float(row[1]))
    	total_votes += 1
    	#total_profit_losses += int(row[1])
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

percent_Khan = float((total_Khan * 100) / total_votes)
percent_Correy =  float((total_Correy * 100) / total_votes)
percent_Li =  float((total_Li * 100) / total_votes)
percent_Tooley =  float((total_Tooley * 100) / total_votes)


list_total_votes.insert(0,total_Khan)
list_total_votes.insert(1,total_Correy)
list_total_votes.insert(2,total_Li)
list_total_votes.insert(3,total_Tooley)

#print (list_total_votes)
winner_total = max(list_total_votes)
winner_index = list_total_votes.index(winner_total)
winner_name = list_candidates[winner_index]

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




