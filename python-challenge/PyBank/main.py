import os
import csv
import statistics

csvpath = os.path.join('Resources', 'budget_data.csv')

csvdata = open(csvpath)

csv_reader = csv.reader(csvdata, delimiter=",")
header = next(csvdata)

netprofit = 0
netprofitlist = []
netchange = []
months = []
monthscount = 0
maxp = ["", 0]
maxl = ["", 0]

for row in csv_reader:
    months.append(row[0])
    netprofitlist.append(row[1])
    netprofit += int(row[1])

monthscount = len(months)

for i in range(len(netprofitlist)-1):
    netchange.append(int(netprofitlist[i+1])-int(netprofitlist[i]))

avgchange = round(sum(netchange)/(len(months)-1), 2)

months.pop(0)

maxpmonth = netchange.index(max(netchange))
maxlmonth = netchange.index(min(netchange))

maxp = (months[int(maxpmonth)], max(netchange))
maxl = (months[int(maxlmonth)], min(netchange))

print("Financial Analysis")
print("-------------------------------")
print(f"Total Months: {monthscount}")
print(f"Total Profits/Losses: ${netprofit}")
print(f"Average  Change: ${avgchange}")
print(f"Greatest Increase in Profits: {maxp}")
print(f"Greatest Decrease in Profits: {maxl}")
print("-------------------------------")

with open('Analysis/final_analysis.txt', 'w') as outputtxt:
    outputtxt.write("Financial Analysis\n\n")
    outputtxt.write("-------------------------------\n\n")
    outputtxt.write(f"Total Months: {monthscount}\n")
    outputtxt.write(f"Total Profits/Losses: ${netprofit}\n")
    outputtxt.write(f"Average  Change: ${avgchange}\n")
    outputtxt.write(f"Greatest Increase in Profits: {maxp}\n")
    outputtxt.write(f"Greatest Decrease in Profits: {maxl}\n\n")
    outputtxt.write("-------------------------------")