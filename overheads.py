from pathlib import Path
import csv

# create a file to csv file.
fp = Path.cwd()/"csv_reports"/"overheads.csv"

# read the csv file to append profit and quantity from the csv.
with fp.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    next(reader) # skip header

    # create an empty lists to store the type of expense and its percentage
    overheads=[] 

    # append type of expense and its percentage into the overheads list
    for row in reader:
        #get the type of expense and its percentage
        #and append the overheads list
        overheads.append([row[0],row[1]])  