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

    # append the day and the respective net profit into the profitLoss list
    for row in reader:
        # get day and its respective net profit
        # and append the profitLoss list
        profitLoss.append([str(row[0]), str(row[4])])

#-------------------------------------------------------------#

def profitLoss_function(profitLoss):
    previous_net_profit = None
    highest_increment = {'day': None, 'amount': 0}

    # create a new variable to store the output
    output = ""

    for day, net_profit in profitLoss:
        # convert cash value to integer
        net_profit = int(net_profit)

        # determines whether difference is a deficit or a surplus
        if previous_net_profit is not None:
            # subtract the current day's net profit from the previous day's net profit
            net_profit_diff = net_profit - previous_net_profit

            # if the difference is below 0 (a negative number), it is a deficit
            if net_profit_diff < 0:
                output += f"[NET PROFIT DEFICIT] Day: {day}, Amount: USD{abs(net_profit_diff)}\n"

            # if the difference is above 0 (a psoitive number), it is a surplus
            else:
                output += f"[NET PROFIT SURPLUS] Day: {day}, Amount: USD{net_profit_diff}\n"

                if net_profit_diff > highest_increment['amount']:
                    # to find out day with the highest increment
                    highest_increment['day'] = day
                    highest_increment['amount'] = net_profit_diff

        # the current day's net profit will become the previous day's net profit as the code loops
        previous_net_profit = net_profit

    if highest_increment['day'] is not None:
        output += f"[HIGHEST NET PROFIT SURPLUS] Day: {highest_increment['day']}, Amount: USD{highest_increment['amount']}"

    # return all the outputs
    return output