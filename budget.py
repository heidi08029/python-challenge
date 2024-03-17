import os
import csv

#specify the file to open
csvpath = os.path.join("budget_Data.csv")

#open file
with open(csvpath,"r") as file:
    data = csv.reader(file)

#first line is header
    next(data,None)

#create list for each row in CSV file
    Month =[]
    Revenue =[]
    
    for row in data:
        Month.append(row[0])
        Revenue.append(row[1])
    print ("Financial Analysis")
    print ("----------------------------------------------")
    print (f"Total Months: {len(Month)}")

#convert string to integers
    Revenue = list(map(int,Revenue))

#calcuate the total profit
    total_profit= 0
    for i in Revenue:
        total_profit = total_profit + i
    print (f"Total: ${total_profit}")

#create a list for the revenue change
    revenue_change = []
    for i in range(len(Revenue)-1):
        revenue_change.append(Revenue[i+1]-Revenue[i])

#calcuate average of revenue change
    total_revenue_change = 0
    for i in revenue_change:
        total_revenue_change = total_revenue_change +i
    average_change = round(total_revenue_change / len(revenue_change),2)
    print (f"Average Change: $ {average_change}")

#calcuate the greatest change increase and decrease
    max_change = max(revenue_change)
    month_max = Month[revenue_change.index(max_change)+1]
    min_change = min(revenue_change)
    month_min = Month[revenue_change.index(min_change)+1]
    print (f"Greatest Increase in profits: {month_max} (${max_change})")
    print (f"Greatest Decrease in Profits: {month_min} (${min_change})")

#output to text file
    f = open("output_budget.txt",'w')
    print ("Financial Analysis",file=f)
    print ("----------------------------------------------",file=f)
    print (f"Total Months: {len(Month)}",file=f)
    print (f"Total: ${total_profit}",file=f)
    print (f"Average Change: $ {average_change}",file=f)
    print (f"Greatest Increase in profits: {month_max} (${max_change})",file=f)
    print (f"Greatest Decrease in Profits: {month_min} (${min_change})",file=f)
#reference: to convert output to Text: https://www.youtube.com/watch?v=FNOpWah3saA&t=35s 