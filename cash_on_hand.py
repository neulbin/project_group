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
        # get the day and its amount of cash on hand
        # and append the cashOnHand list
        cashOnHand.append([str(row[0]), str(row[1])])

#-------------------------------------------------------------#

def coh_function(cashOnHand):
    previous_cash = None
    highest_surplus = {'day': None, 'amount': 0}

    # create a new variable to store the output
    output = ""

    for day, cash in cashOnHand:
        # convert cash value to integer
        cash = int(cash)

        # determines whether difference is a deficit or a surplus
        if previous_cash is not None:
            # subtract the current day's cash on hand from the previous day's cash on hand
            cash_diff = cash - previous_cash
            
            # if the difference is below 0 (a negative number), it is a deficit
            if cash_diff < 0:
                output += f"[CASH DEFICIT] Day: {day}, Amount: USD{abs(cash_diff)}\n"

            # if the difference is above 0 (a psoitive number), it is a surplus
            else:
                output += f"[CASH SURPLUS] Day: {day}, Amount: USD{cash_diff}\n"

                # to find out day with the highest surplus
                if cash_diff > highest_surplus['amount']:
                    highest_surplus['day'] = day
                    highest_surplus['amount'] = cash_diff

        # the current day's cash on hand will become the previous day's cash on hand as the code loops
        previous_cash = cash

    if highest_surplus['day'] is not None:
        output += f"[HIGHEST CASH SURPLUS] Day: {highest_surplus['day']}, Amount: USD{highest_surplus['amount']}"

    # return all the outputs
    return output