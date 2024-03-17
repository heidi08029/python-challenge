import os
import csv

#set path for file
csvpath = os.path.join("election_data.csv")

#open file
with open(csvpath,"r") as file:
    data = csv.reader(file)
    
#first line is header
    next(data,None)

    voterID=[]
    county =[]
    candidate = []

    for row in data:
        voterID.append(row[0])
        county.append(row[1])
        candidate.append(row[2])
    total_votes = len(voterID)

    Charles = 0
    Diana = 0
    Raymon = 0

    for i in candidate:
        if i == "Charles Casper Stockham":
            Charles = Charles + 1
        elif i == "Diana DeGette":
            Diana = Diana + 1
        elif i == "Raymon Anthony Doane":
            Raymon = Raymon +1
    
    percentage_Charles = round (Charles / total_votes *100,3)
    percentage_Diana = round (Diana / total_votes *100,3)
    percentage_Raymon = round (Raymon / total_votes*100,3)
    
    print ("Election Results")
    print ("-------------------------------------")
    print (f"Total Votes: {total_votes}")
    print ("-------------------------------------")
    print (f"Charles Casper Stockham: {percentage_Charles}% ({Charles})")
    print (f"Diana DeGette: {percentage_Diana}% ({Diana})")
    print (f"Raymon Anthony Doane: {percentage_Raymon}% ({Raymon})")
    print ("-------------------------------------")

    if Charles>Diana and Charles>Raymon:
        print ("Winner: Cahrles Casper Stockham")
    elif Diana>Charles and Diana>Raymon:
        print("Winner: Diana DeGette")
    elif Raymon>Diana and Raymon>Charles:
        print ("Winner: Raymon Anthony Doane")
    print ("-------------------------------------")
    
#convert to text
    f = open("output_election.txt",'w')
    print ("Election Results",file=f)
    print ("-------------------------------------",file=f)
    print (f"Total Votes: {total_votes}",file=f)
    print ("-------------------------------------",file=f)
    print (f"Charles Casper Stockham: {percentage_Charles}% ({Charles})",file=f)
    print (f"Diana DeGette: {percentage_Diana}% ({Diana})",file=f)
    print (f"Raymon Anthony Doane: {percentage_Raymon}% ({Raymon})",file=f)
    print ("-------------------------------------",file=f)

    if Charles>Diana and Charles>Raymon:
        print ("Winner: Cahrles Casper Stockham",file=f)
    elif Diana>Charles and Diana>Raymon:
        print("Winner: Diana DeGette",file=f)
    elif Raymon>Diana and Raymon>Charles:
        print ("Winner: Raymon Anthony Doane",file=f)
    print ("-------------------------------------",file=f)
#reference: to convert output to Text: https://www.youtube.com/watch?v=FNOpWah3saA&t=35s