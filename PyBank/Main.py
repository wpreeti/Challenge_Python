import os
import csv
from pathlib import Path

month = []
profitloss = []
monthlychanges = []
monthcount = 0
total = 0

budget_data = os.path.join(Path.home(),"Bootcamp-Homework/Challenge_Python/PyBank/Resources","budget_data.csv")
output_file = os.path.join(Path.home(),"Bootcamp-Homework/Challenge_Python/PyBank/Analysis","PyBank.txt")

with open(budget_data) as csvfile:
    csvreader=csv.reader(csvfile, delimiter =',')
    header=next(csvreader)
    for row in csvreader:
        monthcount +=1
        total +=int(row[1])
        month.append(row[0])
        profitloss.append(int(row[1]))

# first month ProfitLoss value
firstProfitLoss = int(profitloss[0])

# Create list of monthly changes
for i in range (1, len(profitloss)):
    monthlychanges.append(int(profitloss[i])- firstProfitLoss)
    firstProfitLoss = int(profitloss[i])
    i +=1
    
AvgChange = sum(monthlychanges) / len(monthlychanges)

# Find max incraese and min increase  
MaxIncrease = max(monthlychanges)
MaxDecrease = min(monthlychanges)

# Find month index for max increase and max decrease

for i in range(len(monthlychanges)):
    if monthlychanges[i] == MaxIncrease:
        maxIndex = (i+1)
    elif monthlychanges[i] == MaxDecrease:
        minIndex = (i+1)

MaxMonth = month[maxIndex]
MinMonth = month[minIndex]


print("Financial Analysis")
print("-"*50)
print(f"Total Months: {monthcount}")
print(f"Total Amount: ${total}")
print(f"Average Change: ${round(AvgChange,2)}")
print(f"Greatest Increase in Profits: {MaxMonth} (${MaxIncrease})")
print(f"Greatest Decrease in Profits: {MinMonth} (${MaxDecrease})")


# Write into PyBank.txt

with  open(output_file, 'w') as output:
    output.write("Financial Analysis\n")
    output.write("-"*50 + "\n")
    output.write(f"Total Months: {monthcount}\n")
    output.write(f"Total: ${total}\n")
    output.write(f"Average Change: ${round(AvgChange,2)}\n")
    output.write(f"Greatest Increase in Profits: {MaxMonth} (${MaxIncrease})\n")
    output.write(f"Greatest Decrease in Profits: {MinMonth} (${MaxDecrease})")
    
 

    
                           
    

    
