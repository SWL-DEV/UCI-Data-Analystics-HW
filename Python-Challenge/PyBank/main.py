import os
import csv


csvpath = os.path.join('..','Resources', 'budget_data.csv')

date_list = []
total_num_months = 0
net_total_ProfLoss = 0
ProfLoss_list = []


with open(csvpath, newline='') as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=',')

    next(csvreader)

    for row in csvreader:
        
        # Find total number of months
        date_list.append(row[0])
        total_num_months = len(date_list)
        
        # Find total profit/loss
        net_total_ProfLoss += int((row[1]))
        
        # Find average profit/loss
        ProfLoss_list.append(row[1])

        ProfLoss_Change = [int(ProfLoss_list[i + 1]) - int(ProfLoss_list[i]) for i in range(len(ProfLoss_list)-1)]

        Total_Change = sum(ProfLoss_Change)


# Find the greatest increase in profits (date and amount)
#  and the greatest decrease in losses (date and amount)
#  over the entire period
with open(csvpath, newline='') as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=',')

    next(csvreader)
    # Tried to perform the iterations below without opening file 
    #      and reading csv again, but cannot do it.  Not sure why.
    

    # Combine the Date and Profit/Loss columns into a dictionary
    date_amount = dict(zip(date_list, ProfLoss_Change))

    Greatest_inc = min(zip(date_list,ProfLoss_Change))
    Greatest_dec = max(zip(date_list,ProfLoss_Change))

    # Cannot get the data in ProfLoss_Change to be read as integers 
    #   so max and min values can identified properly.

analysis_summary = (
f"Total months: {total_num_months}\n"
f"Total amount: ${net_total_ProfLoss}\n"
f"Average change: {Total_Change/total_num_months}\n"
f"Greatest Increase in Profits: {Greatest_inc}\n"
f"Greatest Decrease in Losses: {Greatest_dec}\n")

print(analysis_summary)

wordpath = os.path.join('..', 'Analysis', 'financial_analysis.txt')

with open(wordpath, "w") as txt_file:
    txt_file.write(analysis_summary)