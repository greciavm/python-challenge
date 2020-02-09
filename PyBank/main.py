#import modules
import os
import csv

#set path for file
pybank_csv = os.path.join('.','budget_data.csv')

#set initial values and list
months = 0
total = 0
values = []
dates = []

#open the csv to read
with open (pybank_csv, newline='') as csvfile:
    
    #specify delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    
    #read the header row first  
    csv_header = next(csvreader)

    #read each row of data after the header
    for row in csvreader:
        #total number of months included in the dataset
        months = months + 1
        #net total amount of "Profit/Losses" over the entire period
        total += int(row[1])
        #each amount as value per row
        value = int(row[1])
        #add each value to the values list
        values.append(value)
        #each date per row
        date = (row[0])
        #add each date to the dates list
        dates.append(date)

    #set list to store differences of values
    differences = []

    #for each row of values without including the first one (place [0])
    for i in range(1,len(values)):
        #difference of current row vs the previous one
        difference=int((values[i])-(values[i-1]))
        #add each difference to the differences list
        differences.append(difference)

    #average of the changes in "Profit/Losses" over the entire period
    avg = round(sum(differences)/(months-1),2)
    
    #greatest increase in profits (date and amount) over the entire period
    max_inc = max(differences)

    #greatest decrease in losses (date and amount) over the entire period
    max_dec = min(differences)

    #find date related to max_inc
    max_inc_date = str(dates[differences.index(max_inc)+1])

    #find date related to max_dec
    max_dec_date = str(dates[differences.index(max_dec)+1])
    
    #print summary
    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months: {months}")
    print(f"Total: ${total}")
    print(f"Average Change: ${avg}")
    print(f"Greatest Increase in Profits: {max_inc_date} (${max_inc})")
    print(f"Greatest Decrease in Profits: {max_dec_date} (${max_dec})")

#create text file in this path
text_file = os.path.join("Financial Analysis.txt")

#write this in text file
with open("Financial Analysis.txt", "w") as text_file:
    print("Financial Analysis", file = text_file)
    print("----------------------------", file = text_file)
    print(f"Total Months: {months}", file = text_file)
    print(f"Total: ${total}", file = text_file)
    print(f"Average Change: ${avg}", file = text_file)
    print(f"Greatest Increase in Profits: {max_inc_date} (${max_inc})", file = text_file)
    print(f"Greatest Decrease in Profits: {max_dec_date} (${max_dec})", file = text_file)