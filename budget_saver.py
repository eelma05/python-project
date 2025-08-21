# This scripts aids in saving the budget summary in a txt file
# I used a function in order to call it in my main file and make the code cleaner
def save_budget_summary(budget_month, monthly_income, after_tax, fixed_expenses, total_fixed_expenses, total_daily_expenses, description, disposable_income, choice, savings):
    with open(f"{budget_month}_budget_summary.txt", "w") as file:
        file.write("--- Budget Summary ---\n")
        file.write(f"Month: {budget_month}\n")
        file.write(f"Monthly Income: {monthly_income:.2f}\n")
        file.write(f"Monthly Income (after tax): {after_tax:.2f}\n")
        file.write("Fixed Expenses Breakdown:\n")
        for name, amount in fixed_expenses.items():
            file.write(f"  {name}: {amount:.2f}\n")
        file.write(f"Total Fixed Expenses: {total_fixed_expenses:.2f}\n")
        file.write(f"Daily Spending Description: {description}\n")
        file.write(f"Approximate Daily Expenses for the month: {total_daily_expenses:.2f}\n")
        file.write(f"Disposable Income: {disposable_income:.2f}\n")
        file.write(f"Savings Plan: {choice}\n")
        if choice == "1":
            file.write(f"50/30/20 Plan - Savings: {savings:.2f}\n")
        elif choice == "2":
            file.write(f"Fixed Custom Threshold Plan - Savings: {savings:.2f}\n")

print("Budget summary saved successfully.")

# To load transactions in a file
def load_transactions(file_path):
    transactions = []
    try:
        with open(file_path, "r") as file:
            for line in file:
                # Assuming each line is a transaction in the format "amount description"
                parts = line.strip().split(" ", 1)
                if len(parts) == 2:
                    amount = float(parts[0])
                    description = parts[1]
                    transactions.append((amount, description))
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except Exception as e:
        print(f"Error loading transactions: {e}")
    return transactions