import os
import csv

csvpath = os.path.join ('Resources', 'budget_data.csv')

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
	# CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    # Read each row of data after the header
    
    for row in csvreader:
    	list_date.append(row[0])
    	list_amount.append(float(row[1]))
    	total_months += 1
    	total_profit_losses += int(row[1])

for list_index in range(len(list_amount)):
  if first_time:
    save_amount = float(list_amount[list_index])
    first_time = False
  else:
    list_average.append(float(list_amount[list_index]) - save_amount)
    save_amount = float(list_amount[list_index])
   	   	
total_list_average = sum(list_average) / len(list_average)

save_min_amount = float(min(list_amount))
save_min_index = list_amount.index(save_min_amount)
save_min_month_year = list_date[save_min_index]

save_min_previous_amount = float(list_amount[save_min_index - 1])

decrease_amount = save_min_amount - save_min_previous_amount

save_max_amount = float(max(list_amount))
save_max_index = list_amount.index(save_max_amount)
save_max_month_year = list_date[save_max_index]

save_max_previous_amount = float(list_amount[save_max_index - 1])

increase_amount = save_max_amount - save_max_previous_amount


print ('Financial Analysis')
print ('------------------------')
print (f'Total Months : {total_months}')
print (f'Total : ${round(total_profit_losses)}')
print (f'Average Change: ${round(total_list_average,2)}')
print (f"Greatest Increase in amounts: {save_max_month_year} (${round(increase_amount)})")
print (f"Greatest Decrease in amounts: {save_min_month_year} (${round(decrease_amount)})")


    