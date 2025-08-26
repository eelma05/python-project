# This module helps predict what the user can save annually.
# It uses savings data from previously saved files
# It loads through the files and conducts a key-word search
# After getting the savings, it gets an average and multiplies it by 12, since they are 12 months in a year


import os # Used for folder navigation and building file paths
import time # Used to simulate loading time

# Define the folder path containing CSV files
folder_path = "C:\\Users\\5300\\OneDrive\\Desktop\\Project"

# Function to get all CSV files in the folder and return them in a list
def get_csv_files(folder_path, min_required=3):
    csv_files = [f for f in os.listdir(folder_path) if f.endswith('.csv')]
    if len(csv_files) < min_required:
        print(f"Not enough CSV files found. At least {min_required} are required.")
        exit()
    return csv_files

# This function loads and conducts a keyword search
def extract_savings(folder_path, keyword="Savings Amount"):
    csv_files = get_csv_files(folder_path) # To get the list of filenames
    total_savings = 0
    file_count = 0 # To count how many files had savings entries

    for filename in csv_files:
        file_path = os.path.join(folder_path, filename)
        print(f"🔄 Loading transactions from {os.path.basename(file_path)}...")
        time.sleep(0.5) # Simulate loading time

        try:
            # A line-by-line search is implemented since my files are in sections
            with open(file_path, 'r', encoding='utf-8') as csvfile:
                for line in csvfile:
                    if keyword.lower() in line.lower():
                        parts = line.strip().split(',')
                        if len(parts) >= 2:
                            try:
                                amount = float(parts[1])
                                total_savings += amount
                                file_count += 1
                                print(f"✅ Found savings entry: {amount:.2f}")
                            except ValueError:
                                print(f"Invalid amount found in line: {line.strip()}")
            print(f"Done: {os.path.basename(file_path)}")
        except FileNotFoundError:
            print(f"File not found: {file_path}")
        except Exception as e:
            print(f"Error reading {file_path}: {e}")

    if file_count == 0:
        print(f"No savings data found. Cannot predict annual savings.")


    print(f"\nTotal savings found: Ksh {total_savings:.2f}")
    return total_savings, file_count

# Uses extracted savings and calculates the annual prediction
def predict_annual_savings(total_savings, file_count):
    if file_count == 0:
        return 0.0
    monthly_average = total_savings / file_count
    annual_prediction = monthly_average * 12

    print(f"\nYour predicted annual savings is: {annual_prediction:.2f}")

    if annual_prediction >= 100000:
        print("🌟 You're on track for a fantastic year of saving!")
    elif annual_prediction >= 50000:
        print("💪 Solid progress! Keep it up.")
    else:
        print("🚀 Every shilling counts—you're building momentum!")

    return round(annual_prediction, 2)

# This script will be run as a standalone script.
if __name__ == "__main__":
    total_savings, file_count = extract_savings(folder_path)
    annual_prediction = predict_annual_savings(total_savings, file_count)