#Name: Dinnara Hitt
#Python-Chalenge
#PyPoll 

import os
import csv

csvpath = os.path.join ('Resources', 'PyPoll_Resources_election_data.csv')
output_path = os.path.join ("Resources", "output_election_data.txt")

total_votes = 0
total_none = 0

dict_candidates = {"Khan":0,"Correy":0,"Li":0,"O'Tooley":0}

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
    		dict_candidates["Khan"] += 1
    	elif row[2] == "Correy" :
    		dict_candidates["Correy"] += 1
    	elif row[2] == "Li" :
    		dict_candidates["Li"] += 1
    	elif row[2] == "O'Tooley":
    		dict_candidates["O'Tooley"] += 1
    	else:
    		total_none += 1

#Calculates percentage of each candidate
percent_Khan = float((dict_candidates["Khan"] * 100) / total_votes)
percent_Correy =  float((dict_candidates["Correy"] * 100) / total_votes)
percent_Li =  float((dict_candidates["Li"]* 100) / total_votes)
percent_Tooley =  float((dict_candidates["O'Tooley"] * 100) / total_votes)

#Get the Winner Name
winner_name = max(dict_candidates,key=dict_candidates.get)


#Print Output
print ('Election Results')
print ('-----------------------------')
print (f'Total votes: {total_votes}')
print ('-----------------------------')
print ("Khan: %.3f" % percent_Khan + "%"+ " (" + str(dict_candidates["Khan"]) + ")")
print ("Correy: %.3f" % percent_Correy + "%" + " (" + str(dict_candidates["Correy"])+ ")")
print ("Li: %.3f" % percent_Li + "%" + " (" + str(dict_candidates["Li"])+ ")")
print ("O'Tooley: %.3f" % percent_Tooley + "%" + " (" + str(dict_candidates["O'Tooley"])+ ")")
print ('-----------------------------')
print (f"Winner: {winner_name}")
print ('-----------------------------')

#Write output in a text file
with open(output_path, 'w') as text_file:

    text_file.write('Election Results' + '\n')
    text_file.write('-----------------------------' + '\n')
    print (f'Total votes: {total_votes}', file=text_file)
    print ('-----------------------------', file=text_file)
    print ("Khan: %.3f" % percent_Khan + "%"+ " (" + str(dict_candidates["Khan"]) + ")", file=text_file)
    print ("Correy: %.3f" % percent_Correy + "%" + " (" + str(dict_candidates["Correy"]) + ")", file=text_file)
    print ("Li: %.3f" % percent_Li + "%" + " (" + str(dict_candidates["Li"]) + ")", file=text_file)
    print ("O'Tooley: %.3f" % percent_Tooley + "%" + " (" + str(dict_candidates["O'Tooley"]) + ")", file=text_file)
    print ('-----------------------------', file=text_file)
    print (f"Winner: {winner_name}", file=text_file)
    print ('-----------------------------', file=text_file)



