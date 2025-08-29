# This script helps visualize how your income is distributed. 
# It calculates how your income is distributed and displays it as a bar chart in the terminal.  

# Function to compute percentages and print a simple bar chart.  
def income_distribution(monthly_income, after_tax,
                         total_fixed_expenses, total_daily_expenses,
                         disposable_income, savings_amount):
    distribution = {
        "Tax" : ((monthly_income - after_tax) / monthly_income * 100),
        "Fixed Expenses": (total_fixed_expenses / monthly_income * 100),
        "Daily Expenses": (total_daily_expenses / monthly_income * 100),
        "Disposable Income": (disposable_income / monthly_income * 100),
        "Savings": (savings_amount / monthly_income * 100)
    }
    formatted_distribution = {k: round(v, 2) for k, v in distribution.items()}

    # To print a summary of income allocation
    print("\n🧮 Income Allocation Breakdown:")
    for category, percent in formatted_distribution.items():
        print(f"{category}: {percent:.2f}%")

    # To print a simple bar chart.
    print("\n📊 Income Allocation Bar Chart:")
    for category, percent in formatted_distribution.items():
        bar = "█" * int(percent // 2)  # Each block = 2%
        print(f"{category.ljust(20)} | {bar} {percent:.2f}%")
    
    return formatted_distribution

# Save the bar chart in a .png file for better visualization
import matplotlib.pyplot as plt
import os
import itertools

def save_bar_chart(formatted_distribution, budget_month):
    # The charts will be saved in a folder called "charts"
    os.makedirs("charts", exist_ok=True)
    filename = f"charts/{budget_month}_Progress_chart.png"

    # Sorted distribution by percentage
    sorted_distribution = dict(sorted(formatted_distribution.items(), key=lambda item: item[1], reverse=True))

    categories = list(sorted_distribution.keys())
    percentages = list(sorted_distribution.values())

    plt.figure(figsize=(10, 6))
    # Used category-specific colors
    color_palette = ['red', 'lightskyblue', 'lightgreen', 'yellow', 'pink', 'orange', 'purple']
    colors = list(itertools.islice(itertools.cycle(color_palette), len(categories)))
    plt.barh(categories, percentages, color=colors)

    # Added percentage labels on bars
    for index, value in enumerate(percentages):
        plt.text(value + 1, index, f"{value:.2f}%", va='center')
    plt.xlabel('Percentage')
    plt.title(f'{budget_month} Income Distribution')
    plt.xlim(0, 100)
    plt.xticks(range(0, 101, 10))
    plt.grid(axis='x')

    # Save the figure
    plt.savefig(filename)
    plt.tight_layout()
    print(f"\nBar chart saved successfully as '{filename}'.")
    plt.close()
