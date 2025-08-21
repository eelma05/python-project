# This script has the savings plan
# There will be two options 50/30/20 and fixed custom threshold
# 50/30/20 Plan: Allocates 20% to savings
# Fixed Custom Threshold: User-defined fixed amount to save, e.g I want to save $100

# Import disposable income which will determine if the user can save
from input_handler import disposable_income


# Checks if user is able to save by looking at disposable income
if disposable_income <= 0:
    print("\n You currently have a negative disposable income.")
    print("Unfortunately, you can't save right now. Consider reviewing your expenses.")
else:
    print("\nChoose a savings plan:")
    print("1. 50/30/20")
    print("2. Fixed Custom Threshold")


# Calculate savings  based on the choosen plan
choice = input("Enter the number of your choice: ")
def savings_plan(choice):
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
    else:
        print("Invalid choice. Please select a valid savings plan.")
        return None
    return savings