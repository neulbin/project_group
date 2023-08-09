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

#-------------------------------------------------------------#
def coh_function(cashOnHand):
    previous_cash = None
    highest_surplus = {'day': None, 'amount': 0}

    output = ""

    for day, cash in cashOnHand:
        # convert cash value to integer
        cash = int(cash)

        # determines whether difference is a deficit or a surplus
        if previous_cash is not None:
            cash_diff = cash - previous_cash
            if cash_diff < 0:
                output += f"[CASH DEFICIT] Day: {day}, Amount: USD{abs(cash_diff)}\n"
            else:
                output += f"[CASH SURPLUS] Day: {day}, Amount: USD{cash_diff}\n"
                if cash_diff > highest_surplus['amount']:
                    highest_surplus['day'] = day
                    highest_surplus['amount'] = cash_diff
        previous_cash = cash

    if highest_surplus['day'] is not None:
        output += f"[HIGHEST CASH SURPLUS] Day: {highest_surplus['day']}, Amount: USD{highest_surplus['amount']}"

    return output