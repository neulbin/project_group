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
        # get the type of expense and its percentage
        # and append the overheads list
        overheads.append([row[0],row[1]])  

#-------------------------------------------------------------#

def overhead_function():
    highest_overhead_category = None
    max_expense = 0 

    for category, expense in overheads:
        # convert the percentage of the expense from a string to a float
        expense_percentage = float(expense)

        # compare current expense_percentage to max_expense
        if expense_percentage > max_expense:
            # if current expense_percentage is greater than max_expense
            # update max_expense to the new value and store the category
            max_expense = expense_percentage
            highest_overhead_category = category

        return highest_overhead_category, expense_percentage