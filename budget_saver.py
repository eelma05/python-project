# This scripts aids in saving the budget summary in a csv file
# I used a function in order to call it in my main file and make the code cleaner

# Import csv to aid in writing CSV files
import csv

# Import date to add the timestamp feature to my csv files
from datetime import date

def save_budget_summary(budget_month, monthly_income, after_tax,
                         fixed_expenses, total_fixed_expenses, 
                         daily_spending, total_daily_expenses, description,
                         disposable_income, savings_type, savings_amount):
    
    filename = f"{budget_month}_budget_summary.csv"
    today = date.today().isoformat() # Format the date as YYYY-MM-DD

    try:
        with open(filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)

            # Vertical summary section
            writer.writerow(["Budget Summary"])
            writer.writerow([f"Generated on: {today}"])

            writer.writerow(["Field", "Value"])

            writer.writerow(["Month", budget_month])
            writer.writerow(["Monthly Income", f"{monthly_income:.2f}"])
            writer.writerow(["After Tax Income", f"{after_tax:.2f}"])
            writer.writerow(["Total Fixed Expenses", f"{total_fixed_expenses:.2f}"])
            writer.writerow(["Total Daily Expenses", f"{total_daily_expenses:.2f}"])
            writer.writerow(["Disposable Income", f"{disposable_income:.2f}"])

            # Savings details
            writer.writerow([])
            writer.writerow(["Savings Summary"])
            writer.writerow(["Savings Type", savings_type])
            writer.writerow(["Savings Amount", f"{savings_amount:.2f}"])

            # Fixed expenses breakdown
            writer.writerow([])
            writer.writerow(["Fixed Expenses Breakdown"])
            writer.writerow(["Name", "Amount"])
            for name, amount in fixed_expenses.items():
                writer.writerow([name.strip().title(), f"{amount:.2f}"])

            # Daily spending description
            writer.writerow([])
            writer.writerow(["Daily Spending Description"])
            writer.writerow([description.strip(), daily_spending])

            # Footer
            writer.writerow([])
            writer.writerow(["Thank you for using BudgetBuddy 💖!"])

        print(f"Budget summary saved successfully to {filename}")

    except Exception as e:
        print(f"Error saving CSV: {e}")
