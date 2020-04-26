import os
import csv

# read the file
current_directory = os.getcwd()
csvPath = os.path.join(current_directory,'Resources', 'budget_data.csv')
total_month = 0
total_revenue = 0
revenue_change = 0
previous_revenue = 0
month_change = []
greatestIncrease = ["",0]
greatestDecrease = ["", 999999999]
revenue_list = []


    
with open(csvPath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csvHeader = next(csvreader)
    for row in csvreader:
        month = row[0]
        revenue = int(row[1])
        
    # Totaling the number of months 
        total_month = total_month + 1

    # Totaling the Revenue(Profit/Loss)
        total_revenue = total_revenue + revenue

    # Revenue Changes
        revenue_change = revenue - previous_revenue
        previous_revenue = revenue
        month_change = month_change + [month]
        revenue_list = revenue_list + [revenue_change]

        # Greatest Increase Profit Value
        if (revenue_change > greatestIncrease[1]):
            greatestIncrease[0] = month
            greatestIncrease[1] = revenue_change
            
        
        if (revenue_change < greatestDecrease[1]):
            greatestDecrease[0] = month
            greatestDecrease[1] = revenue_change
            


revenue_avg = round(sum(revenue_list) / len(revenue_list), 2)

def Result():
    print("\tFinancial Analysis")
    print("\t---------------------\n")
    print(f'Total Months: {total_month}\n')
    print(f'Total: ${total_revenue}\n')
    print(f'Average Change: ${revenue_avg}\n')
    print(f'Greatest Increase in Profits: {greatestIncrease[0]} ${greatestIncrease[1]}\n')
    print(f'Greatest Decrease in Losses: {greatestDecrease[0]} ${greatestDecrease[1]}\n')

Result()

output = open("PyBank_output.txt", "w")
output.write("\tFinancial Analysis\n")
output.write("\t---------------------\n")
output.write(f'Total Months: {total_month}\n')
output.write(f'Total: ${total_revenue}\n')
output.write(f'Average Change: ${revenue_avg}\n')
output.write(f'Greatest Increase in Profits: {greatestIncrease[0]} ${greatestIncrease[1]}\n')
output.write(f'Greatest Decrease in Losses: {greatestDecrease[0]} ${greatestDecrease[1]}\n')
