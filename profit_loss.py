from pathlib import Path
import csv

# create a file to csv file.
fp = Path.cwd()/"csv_reports"/"profit_loss.csv"

# read the csv file to append profit and quantity from the csv.
with fp.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    next(reader) # skip header

    # create an empty lists to store the day and the respective net profit
    profitLoss=[] 

    # append the day and the respective net profit record into the salesRecords list
    for row in reader:
        #get day and its respective net profit
        #and append the pro list
        profitLoss.append([row[0],row[4]])