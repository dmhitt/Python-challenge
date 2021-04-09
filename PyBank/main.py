#Name: Dinnara Hitt
#Python-Challenge
#PyBank

import os
import csv

csvpath = os.path.join ('Resources', 'budget_data.csv')
output_path = os.path.join ("output_budget_data.txt")

list_date = []
list_amount = []

total_months = 0
total_profit_losses = 0.00

first_time = True
save_amount = 0.00
list_average = []
total_list_average = 0.00

save_min_amount = 0.00
save_min_index = 0
save_min_month_year = "Jan-2010"
save_min_previous_amount = 0.00
decrease_amount = 0.00

save_max_amount = 0.00
save_max_index = 0
save_max_month_year = "Jan-2010"
save_max_previous_amount = 0.00
increase_amount = 0.00

with open(csvpath) as csvfile:
	
    csvreader = csv.reader(csvfile, delimiter=',')

    # read the header row first 
    csv_header = next(csvreader)
    
    # for loop to read each row of data after the header 
    # saves the date into list_date and saves amount into list_amount
        
    for row in csvreader:
    	list_date.append(row[0])
    	list_amount.append(float(row[1]))
    	total_months += 1
    	total_profit_losses += int(row[1])

# for loop that saves the average of two amounts into a list_average 
for list_index in range(len(list_amount)):
  if first_time:
    save_amount = float(list_amount[list_index])
    first_time = False
  else:
    list_average.append(float(list_amount[list_index]) - save_amount)
    save_amount = float(list_amount[list_index])
   	   	
# calculates the average change
total_list_average = sum(list_average) / len(list_average)

#-----Calculate Decrease in Profits--------
#get the min amount to calculate the decrease in profit
save_min_amount = float(min(list_amount))

#gets the index of the min amount to use to retrieve the date from list_date  and previous amount
save_min_index = list_amount.index(save_min_amount)

#gets the date for the decrease in profit
save_min_month_year = list_date[save_min_index]
 
#gets the amount before the min to calculate the decrease in profit
save_min_previous_amount = float(list_amount[save_min_index - 1])

decrease_amount = save_min_amount - save_min_previous_amount

#-----Calculate Increse in Profits--------
#gets the max amount to calculate the increase in profit
save_max_amount = float(max(list_amount))

#gets the index of the max amount to use to retrieve the date from list_date  and previous amount
save_max_index = list_amount.index(save_max_amount)

#gets the date for the increase in profit
save_max_month_year = list_date[save_max_index]

#gets the amount before the max to calculate the increase in profit
save_max_previous_amount = float(list_amount[save_max_index - 1])

increase_amount = save_max_amount - save_max_previous_amount

#Print Output
print ('Financial Analysis')
print ('------------------------')
print (f'Total Months : {total_months}')
print (f'Total : ${round(total_profit_losses)}')
print (f'Average Change: ${round(total_list_average,2)}')
print (f"Greatest Increase in amounts: {save_max_month_year} (${round(increase_amount)})")
print (f"Greatest Decrease in amounts: {save_min_month_year} (${round(decrease_amount)})")

#Write output in a text file
with open(output_path, 'w') as text_file:

	text_file.write("Financial Analysis" + '\n')
	text_file.write('------------------------' + '\n')
	print(f"Total Months : {total_months}", file=text_file)
	print(f'Total : ${round(total_profit_losses)}', file=text_file)
	print(f'Average Change: ${round(total_list_average,2)}', file=text_file)
	print(f"Greatest Increase in amounts: {save_max_month_year} (${round(increase_amount)})", file=text_file)
	print(f"Greatest Decrease in amounts: {save_min_month_year} (${round(decrease_amount)})", file=text_file)





