from pathlib import Path
import csv

# create a file to csv file.
fp = Path.cwd()/"csv_reports"/"cash_on_hand.csv"

# read the csv file to append profit and quantity from the csv.
with fp.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    next(reader) # skip header

    # create an empty lists to store the day and the respective amount of cash on hand
    cashOnHand=[] 

    # append the day and the respective amount of cash on hand into the cashOnHand list
    for row in reader:
        #get the day and its amount of cash on hand
        #and append the cashOnHand list
        cashOnHand.append([row[0],row[1]])   