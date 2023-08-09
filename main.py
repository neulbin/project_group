from pathlib import Path
import cash_on_hand, overheads, profit_loss

highest_overhead_category, expense_percentage = overheads.overhead_function()
cashOnHand = cash_on_hand.cashOnHand
profitLoss = profit_loss.profitLoss

# create a file path and a new file.txt
file_path_write = Path.cwd()/'summary_report.txt'
file_path_write.touch()

with file_path_write.open(mode='w', encoding="'UTF-8") as file:
    # write the highest overhead category
    file.write(f"[HIGHEST OVERHEAD CATEGORY] {highest_overhead_category}: {expense_percentage}%\n")

    # write a divider
    file.write("----------------------------------------------\n")

    # write the output of coh_function
    file.write(f"{cash_on_hand.coh_function(cashOnHand)}\n")
    # write a divider
    file.write("----------------------------------------------\n")

    #write the output of profitLoss_function
    file.write(profit_loss.profitLoss_function(profitLoss))