# This script has the suggested savings, savings plan and savings messages.
# Suggested savings will be based on their disposable income
# To make things simpler, if disposable income is greater than 20000 the app suggests for you and if it is less than you have to choose a plan.
# There will be two savings plan options 50/30/20 and fixed custom threshold.
# 50/30/20 Plan: Allocates 20% to savings
# Fixed Custom Threshold: User-defined fixed amount to save, e.g I want to save $100


# If user qualifies for suggested plan, the app suggests savings 50% of the disposable income.
def suggest_savings(disposable_income):
    print("\n💰--- Suggested Savings ---")
    rate = 0.5
    suggested = disposable_income * rate 
    print(f"\nBased on your disposable income, we suggest saving: {suggested:.2f} ({int(rate*100)}%)")
    return suggested


# Calculate savings  based on the choosen plan
def savings_plan(disposable_income):
    choice = input("Enter the number of your choice: ")
    if choice == "1":
        # 50/30/20 plan
        savings = disposable_income * 0.2
        print("\n💰--- 50/30/20 Savings Plan ---")
        print(f"Savings: {savings:.2f}")
    elif choice == "2":
    # Fixed Custom Threshold
        while True:
            try:
                custom_threshold = float(input("Enter fixed amount to save (e.g. I want to save $100): "))
                # Ensure the custom threshold is not more than disposable income
                if 0 <= custom_threshold <= disposable_income:
                    savings = custom_threshold
                    print("\n💰--- Fixed Custom Threshold Savings Plan ---")
                    print(f"Savings: {savings:.2f}")
                    break
                else:
                    print("Please enter a valid threshold.")
            except ValueError:
                print("Invalid input. Please enter a number.")
    else:
        print("Invalid choice. Please select a valid savings plan.")
        return None
    savings_type = "50/30/20 Plan" if choice == "1" else "Custom Threshold Plan"
    savings_amount = savings
    return savings_type, savings_amount

# Display a message based on the savings amount
def savings_message(savings_amount):
    if savings_amount >= 10000:
        message = "🌟 That’s a fantastic savings amount—your future self will thank you!"
    elif savings_amount >= 5000:
        message = "👍 Solid savings! Keep building that momentum."
    elif savings_amount > 0:
        message = "👏 Every bit counts. Consistency is key."
    print(message)
    return message
