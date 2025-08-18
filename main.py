# Get the specific month we are budgeting for
def get_budget_month():
    while True:
        month = input("Enter the month you are budgeting for (e.g., January, February, etc.): ").strip().capitalize()
        if month:
            return month
        else:
            print("Invalid input. Please enter a valid month name.")

budget_month = get_budget_month()


# Get the user's monthly income using a function
def get_monthly_income():
    while True:
        monthly_income_str = input("Enter your monthly income (default 0): ")
        if not monthly_income_str:
            return 0.0
        try:
            monthly_income = float(monthly_income_str)
            return monthly_income
        except ValueError:
            print("Invalid input. Please enter a number like 12000 or 12000.50.")

monthly_income = get_monthly_income()


# Deduct taxes if any
def get_tax_rate():
    tax_user = (input("Do you have to pay taxes? (yes/no): ").strip().lower() == "yes")
    if tax_user:
        while True:
            try:
                tax_rate = float(input("Enter your tax rate (as a percentage, e.g., 20 for 20%): "))
                if 0 <= tax_rate <= 100:
                    after_tax = monthly_income * (1 - tax_rate / 100)
                    return after_tax
                else:
                    print("Please enter a valid tax rate between 0 and 100.")
            except ValueError:
                print("Invalid input. Please enter a number like 20 or 20.5.")
  
    else:
        after_tax = monthly_income

    return after_tax

after_tax = get_tax_rate()

# Get fixed monthly expenses
fixed_expenses = {}
expense_types = ["rent", "electricity", "water", "shopping", "fuel"]
print("Enter your monthly fixed expenses (leave blank if not applicable):")

for expense in expense_types:
    amount_str = input(f"{expense.capitalize()}: ")
    try:
        amount = float(amount_str) if amount_str else 0.0
        if amount > 0:
            fixed_expenses[expense] = amount
    except ValueError:
        print("Invalid input, skipping.")
   

# To get additional  fixed monthly expenses
add_more = (input("Do you have any other fixed expenses? (yes/no): ").strip().lower() == "yes")
while add_more:
    name = input("Enter the name of the expense: ")
    while True:
        try:
            amount = float(input(f"Enter your monthly {name} expense: "))
            fixed_expenses[name] = amount
            break
        except ValueError:
            print("Please enter a valid number.")
    # Ask if the user wants to add more expenses
    add_more = (input("Add another fixed expense? (yes/no): ").strip().lower() == "yes")

# Calculate total fixed monthly expenses
total_fixed_expenses = sum(fixed_expenses.values()) 

# Get an estimate of daily spendings and a description using a function
def daily_spending_estimate():
    daily_spending_str = input("How much do you spend daily and on what? (e.g., 300 food/transport): ")
    if not daily_spending_str:
        return 0.0, ""
    # Split the input into parts to separate amount and description
    parts = daily_spending_str.split()
    if parts:
     try:
        daily_spending = float(parts[0])
        description = " ".join(parts[1:]) if len(parts) > 1 else ""
     except ValueError:
        daily_spending = 0.0
        description = ""
    return daily_spending, description
   
   
daily_spending, description = daily_spending_estimate()

# Get total monthly daily expenses
total_daily_expenses = daily_spending * 30  # Approximate a month as 30 days

# Get disposable income, which is the income left after all expenses
disposable_income = after_tax - total_fixed_expenses - total_daily_expenses

# Display the budget summary
print("\n--- Budget Summary ---")
print(f"Month: {budget_month}")
print(f"Monthly Income: {monthly_income:.2f}")
print(f"Monthly Income (after tax): {after_tax:.2f}")
print(f"Total Fixed Expenses: {total_fixed_expenses:.2f}")
print(f"Total Daily Expenses: {total_daily_expenses:.2f}")
print(f"Disposable Income: {disposable_income:.2f}")

# Prompt the user to pick a savings plan to save money
# There will be two options 50/30/20 and fixed custom threshold
print("\nChoose a savings plan:")
print("1. 50/30/20")
print("2. Fixed Custom Threshold")

# Calculate savings  based on the choosen plan
choice = input("Enter the number of your choice: ")
if choice == "1":
    # 50/30/20 plan
    savings = disposable_income * 0.2
    print("\n--- 50/30/20 Savings Plan ---")
    print(f"Savings: {savings:.2f}")
elif choice == "2":
    # Fixed Custom Threshold
    while True:
        try:
            custom_threshold = float(input("Enter fixed amount to save (e.g. I want to save $100): "))
            # Ensure the custom threshold is not more than disposable income
            if 0 <= custom_threshold <= disposable_income:
                savings = custom_threshold
                print("\n--- Fixed Custom Threshold Savings Plan ---")
                print(f"Savings: {savings:.2f}")
                break
            else:
                print("Please enter a valid threshold.")
        except ValueError:
            print("Invalid input. Please enter a number.")

# Inform the user that we will store the budget data in a file
print(f"\nYour budget data will be stored in '{budget_month}_budget_summary.txt'.")

# Save the budget summary to a text file
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