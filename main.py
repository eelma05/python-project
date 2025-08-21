# Import necessary functions and variables from input_handler
from input_handler import get_budget_month, get_monthly_income, get_after_tax_income
from input_handler import fixed_expenses_dict as fixed_expenses 
from input_handler import total_fixed_expenses
from input_handler import total_daily_expenses, description, disposable_income

# Call the functions that we imported 
budget_month = get_budget_month()
monthly_income = get_monthly_income()
after_tax = get_after_tax_income(monthly_income)

# Display the budget summary
print("\n--- Budget Summary ---")
print(f"Month: {budget_month}")
print(f"Monthly Income: {monthly_income:.2f}")
print(f"Monthly Income (after tax): {after_tax:.2f}")
print(f"Total Fixed Expenses: {total_fixed_expenses:.2f}")
print(f"Total Daily Expenses: {total_daily_expenses:.2f}")
print(f"Disposable Income: {disposable_income:.2f}")

# Import savings_plan from savings 
from savings import savings_plan 
from savings import choice

# Call the savings_plan function to calculate savings based on user choice
saving_choice = savings_plan(choice)

# Inform the user that we will store the budget data in a file
print(f"\nYour budget data will be stored in '{budget_month}_budget_summary.txt'.")

# Import save_budget_summary function from budget_saver to save the budget in a text file
from budget_saver import save_budget_summary

# Call the function to save the budget summary
save_budget_summary(budget_month, monthly_income, after_tax, fixed_expenses, total_fixed_expenses, total_daily_expenses, description, disposable_income, choice, saving_choice)