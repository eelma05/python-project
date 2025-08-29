# This file handles input from the user
# It also calculates total expenses and income

# Get the specific month we are budgeting for
def get_budget_month():
    month_map = {
    "Jan": "January", "Feb": "February", "Mar": "March", "Apr": "April",
    "May": "May", "Jun": "June", "Jul": "July", "Aug": "August",
    "Sep": "September", "Oct": "October", "Nov": "November", "Dec": "December"
    } # The map is used to ensure the user inputs a valid month name or short form.

    while True:
        month = input("Enter the month you are budgeting for (e.g., January, February, etc.): ").strip().title()
        if month in month_map.values():
            return month
        elif month in month_map.keys():
            return month_map[month]
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
def get_after_tax_income(monthly_income):
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

after_tax = get_after_tax_income(monthly_income)



# Get fixed monthly expenses
fixed_expenses_dict = {}
expense_types = ["rent", "electricity", "water", "shopping", "fuel"]
print("Enter your monthly fixed expenses (leave blank if not applicable):")

for expense in expense_types:
    amount_str = input(f"{expense.capitalize()}: ")
    try:
        amount = float(amount_str) if amount_str else 0.0
        if amount > 0:
            fixed_expenses_dict[expense] = amount
    except ValueError:
        print("Invalid input, skipping.")
        # If the input is invalid, we skip adding this expense
   

# To get additional  fixed monthly expenses
add_more = (input("Do you have any other fixed expenses? (yes/no): ").strip().lower() == "yes")
while add_more:
    name = input("Enter the name of the expense: ")
    while True:
        try:
            amount = float(input(f"Enter your monthly {name} expense: "))
            fixed_expenses_dict[name] = amount
            break
        except ValueError:
            print("Please enter a valid number.")
    # Ask if the user wants to add more expenses
    add_more = (input("Add another fixed expense? (yes/no): ").strip().lower() == "yes")

# Calculate total fixed monthly expenses
total_fixed_expenses = sum(fixed_expenses_dict.values()) 

#  Prompt the user for their estimated daily spending and a description, returning both as a tuple.
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
# Assumption: A month is approximated as 30 days. 
month_days = 30
total_daily_expenses = daily_spending * month_days 

# Get disposable income, which is the income left after all expenses
disposable_income = after_tax - total_fixed_expenses - total_daily_expenses
