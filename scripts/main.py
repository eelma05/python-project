# This is the main script that connects all components
# A welcome message, brief instructions and a quote will be displayed first before prompting the user for input

import random

quotes = [
    "“Do not save what is left after spending, but spend what is left after saving.” ~ Warren Buffett",
    "“A budget is telling your money where to go instead of wondering where it went.” ~ Dave Ramsey",
    "“Beware of little expenses; a small leak will sink a great ship.” ~ Benjamin Franklin",
    "“Financial freedom is available to those who learn about it and work for it.” ~ Robert Kiyosaki",
    "“The goal isnt more money. The goal is living life on your terms.” ~ Chris Brogan",
    "“Budgeting isnt about limiting yourself—its about making the things that matter possible.” ~ Unknown",
    "“Financial peace isnt the acquisition of stuff. Its learning to live on less than you make.” ~ Dave Ramsey",
    "“Save money and money will save you.” ~ Jamaican Proverb",
    "“A budget is more than numbers on a page; its an embodiment of our values.” ~ Barack Obama"
]

def welcome_message():
    print("\n🌟 Welcome to BudgetBuddy 🌟")
    print("Track your income, manage expenses, and grow your savings with clarity.")
    print("You will be required to input details about your income and expenses.")
    print("The details will be stored in a CSV file later on.")
    print("Let's get started!\n")

def show_motivational_quote():
    print("💬 " + random.choice(quotes) + "\n")

def main():
    # Launch sequence
    welcome_message()
    show_motivational_quote()

    # Collect user input
    from input_handler import (
    budget_month, monthly_income, after_tax,
    fixed_expenses_dict as fixed_expenses,
    total_fixed_expenses, total_daily_expenses, 
    daily_spending, description, disposable_income
    )

    # Display the budget summary
    print("\n--- Budget Summary ---")
    print(f"Month: {budget_month}")
    print(f"Monthly Income: {monthly_income:.2f}")
    print(f"Monthly Income (after tax): {after_tax:.2f}")
    print(f"Total Fixed Expenses: {total_fixed_expenses:.2f}")
    print(f"Total Daily Expenses: {total_daily_expenses:.2f}")
    print(f"Disposable Income: {disposable_income:.2f}")

    # Import the two functions that determine savings
    from savings import suggest_savings, savings_plan, savings_message

    # Checks if user is able to save or use suggested savings or choose a plan
    if disposable_income <= 0:
        savings_type = "Not applicable"
        savings_amount = 0.0
        print("\nYou currently have a negative disposable income.")
        print("Unfortunately, you can't save right now. Consider reviewing your expenses.")

    elif disposable_income > 20000:
        # Use suggested savings
        savings_amount = suggest_savings(disposable_income)
        savings_type = "Suggested"

    else:
        # Prompt user to choose a savings plan
        print("\nYour disposable income is below the threshold for auto-suggested savings.")
        print("\nChoose a savings plan:")
        print("1. 50/30/20")
        print("2. Fixed Custom Threshold")
        savings_type, savings_amount = savings_plan(disposable_income)

    # The variable savings_type and savings_amount will aid making the logic dynamic during file saving  

    # Display an encouraging savings message based on savings amount
    savings_message(savings_amount)

    # Display the income distribution bar chart that aids visualize spending patterns.
    from progress_chart import income_distribution
    formatted_distribution = income_distribution(
        monthly_income, after_tax, total_fixed_expenses,
        total_daily_expenses, disposable_income, savings_amount
    ) 

    # Inform the user that we will store the budget data in a file
    print(f"\nYour budget data will be stored in '{budget_month}_budget_summary.csv'.\n")

    # Inform user that the bar chart displayed will be saved in a png file
    print(f"The income distribution chart will be saved in '{budget_month}_Progress_chart.png'.\n")

    # Import save_budget_summary function from budget_saver to save the budget in a csv file
    from budget_saver import save_budget_summary

    # Call the function to save the budget summary
    save_budget_summary(
        budget_month, monthly_income, 
        after_tax, fixed_expenses,
        total_fixed_expenses, daily_spending, total_daily_expenses,
        description, disposable_income, 
        savings_type, savings_amount, formatted_distribution
    )

    # Import and call function to save chart in .png file
    from progress_chart import save_bar_chart
    save_bar_chart(formatted_distribution, budget_month)
    print("All data saved successfully! 🎉")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"🚨 An error occurred: {e}")
