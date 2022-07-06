import csv

csv_file = csv.reader(open("budget_data.csv", 'rescources'))
num_months = len(list(csv_file)) - 1

print("Financial Analysis")
print("----------------------------")
print("Total Months: " + str(num_months))
total = 0
with open('budget_data.csv', newline='')as csvfile:
    data = csv.DictReader(csvfile)
    for row in data:
        total = total + int(row['Profit/Losses'])
print("Total: $" + str(total))

avg_change = 0
past_rev = 0
change = 0
list = []
date_change = []
increase = ["", 0]
decrease = ["", 9999999]

with  open('budget_data.csv', 'resources') as file:
    csvreader = csv.DictReader(file)
    for row in csvreader:
        change = float(row["Profit/Losses"]) - past_rev
        past_rev = float(row["Profit/Losses"])
        list  = list + [change]
        date_change = [date_change] + [row["Date"]]

        if change >  increase[1]:
            increase[1]= change
            increase[0] = row['Date']
        if change < decrease[1]:
            decrease[1] = change
            decrease[0] = row['Date']

    avg_change =  sum(list)/len(list)
print("Average Change: $" + str(avg_change))
print("Greatest Increase in Profits:" + str((increase[0], increase[1])))
print("Greatest Decrease in Profits:" + str((decrease[0], decrease[1])))
