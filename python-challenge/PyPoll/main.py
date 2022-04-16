import os
import csv

csvpath = os.path.join('Resources', 'election_data.csv')

csvdata = open(csvpath)

csv_reader = csv.reader(csvdata, delimiter=",")
header = next(csvdata)

votes = []
tot_votes = 0
rec_votes = []
khan = 0
correy = 0
li = 0
otooley = 0

for row in csv_reader:
    votes.append(row[0])
    if row[2] == "Khan":
        khan = khan + 1
    elif row[2] == "Correy":
        correy = correy + 1
    elif row[2] == "Li":
        li = li + 1
    elif row[2] == "O'Tooley":
        otooley = otooley + 1

tot_votes = len(votes)

perk = str(round(((khan/tot_votes)*100), 2))
perc = str(round(((correy/tot_votes)*100), 2))
perl = str(round(((li/tot_votes)*100), 2))
pero = str(round(((otooley/tot_votes)*100), 2))

perk = (perk + "%")
perc = (perc + "%")
perl = (perl + "%")
pero = (pero + "%")

canlist = {"Khan": khan, "Correy": correy, "Li": li, "O'Tooley": otooley}

v1 = canlist["Khan"]
v2 = canlist["Correy"]
v3 = canlist["Li"]
v4 = canlist["O'Tooley"]

topvotes = 0
for x,y in canlist.items():
    if y > topvotes:
        topvotes = y
        winner = x

print("Election Results")
print("----------------------------------")
print(f"Total Votes: \t", tot_votes)
print("----------------------------------")
print(f"Khan: \t\t", perk , "-", v1)
print(f"Correy: \t", perc , "-", v2)
print(f"Li: \t\t", perl , "-", v3)
print(f"O'Tooley: \t", pero , "-", v4)
print("----------------------------------")
print(f"Winner: \t", winner)
print("----------------------------------")

with open('Analysis/final_analysis.txt', 'w') as outputtxt:
    outputtxt.write("Election Results")
    outputtxt.write("\n----------------------------------")
    outputtxt.write(f"\nTotal Votes:\t{tot_votes}")
    outputtxt.write("\n----------------------------------")
    outputtxt.write(f"\nKhan:\t\t\t{perk} - {v1}")
    outputtxt.write(f"\nCorrey:\t\t\t{perc} - {v2}")
    outputtxt.write(f"\nLi:\t\t\t\t{perl} - {v3}")
    outputtxt.write(f"\nO'Tooley:\t\t{pero} - {v4}")
    outputtxt.write("\n----------------------------------")
    outputtxt.write(f"\nWinner:\t\t\t{winner}")
    outputtxt.write("\n----------------------------------")