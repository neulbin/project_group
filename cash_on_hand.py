from pathlib import Path
import csv

# create a file to csv file.
fp = Path.cwd()/"csv_reports"/"cash_on_hand.csv"

# read the csv file to append profit and quantity from the csv.
with fp.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    next(reader) # skip header

    # create an empty lists to store the amount of cash on hand
    cashOnHand=[] 

    # append time sheet and sales record into the salesRecords list
    for row in reader:
        #get the employee id, total hours, break hours, and sales for each record
        #and append the salesRecords list
        cashOnHand.append([row[0],row[1]])   