#Modules
import os
import csv

#Setting the path for the file
csvpath = os.path.join("Resources", "budget_data.csv")

#set up variables
months = []
profit_loss = []
change = 0.0
total_months = 0.0
last_month_loss = 0.0
current_loss = 0.0
total_profit_loss = 0.0

#Open the csv file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader) #saving header 

    for row in csvreader:
        total_months += 1
        current_loss = int(row[1])
        total_profit_loss += current_loss
        if total_months == 1:
            last_month_loss = current_loss
        else:
            change = current_loss - last_month_loss
            months.append(row[0])
            profit_loss.append(change)
            last_month_loss = current_loss

    #finding the totals for all loss, as well as finding the average
    sum_p_loss = sum(profit_loss)
    ave_p_loss = round((sum_p_loss / (total_months -1)), 2)

    #increase and decrease in profits 
    increase = max(profit_loss)
    decrease = min(profit_loss)

    #setting the index equal to day/month of profit 
    day_increase = profit_loss.index(increase)
    day_decrease = profit_loss.index(decrease)

    month_increase = months[day_decrease]
    month_decrease = months[day_decrease]

print("Financial Analysis")
print("-------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_profit_loss}")
print(f"Average Change: ${ave_p_loss}")
print(f"Greatest Increase in Profits: {month_increase}-{day_increase} (${increase})")
print(f"Greatest Decrease in Profits: {month_decrease}-{day_decrease} (${decrease})")


