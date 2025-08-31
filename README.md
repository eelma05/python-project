# 💼BudgetBuddy
 
**Track smarter. Save better. Grow consistently.**

My version of a budget tracker app  is your personal financial companion-simple, supportive, and smart.
BudgetBuddy is a user-friendly Python app that enables you to make better financial decisions.BudgetBuddy is more than a tracker. It is a motivational tool that helps you build better habits-one transaction at a time.

## ✅Table of contents

- [Overview](#Overview)
- [Features](#Features)
- [Installation](#Installation)
- [Usage](#Usage)
- [Technologies Used](#Technologies)
- [Contributing](#Contributing)
---

### ✨Overview

This Budget Tracker app is a Python application designed to help individuals manage their finances with clarity and control. It allows users to input income and expenses, and offers savings suggestions based on their disposable income.All data is saved in CSV(Comma-Separated Values) files for simplicity, easy access and future analysis.
The app includes motivational messages and predictive insights, helping users stay inspired while estimating their potential annual savings based on past behavior.
The app is also designed to encourage the users by analyzing their savings amount and predicting their annual savings.

---

### ✨Features

- **Warm Messages & Financial Quotes** 

Displays a welcome message and a randomly selected financial quotes at the beginning to set a positive tone. It also encourages user with savings messages based on their progress.
- **Income & Expense Input**

Collects detailed financial data including monthly income, tax rate, fixed expenses and daily spending via `input_handler.py`.
- **Smart Savings Suggestions**

Recommends savings strategies based on disposabe income. Offers auto-suggestions for high earners and flexible plans for others via [savings.py](scripts/savings.py)`savings.py`.
- **Income Distribution Visualization**

Displays a terminal-based bar chart and saves a PNG chart showing how income is allocated across catergories via `progress_chart.py`
- **Annual Savings Prediction**

Analyzes past CSV summaries to estimate yearly savings based on historical behavior via `predict_savings.py`
- **Dynamic File Saving**

Automatically saves budget data via `budget_saver.py` in CSV files in organized folders for easy tracking.
- **Modular Design**

Clean organized codebase with reusable modules(`main.py`, `input_handler.py`, `savings.py`, etc.) for clarity and maintainability.

---
### ✨Installation

To install and run **BudgetBuddy**, follow these steps:


1. _Clone the Repository_
```bash
git clone https://github.com/eelma05/python-project
cd Project
```

2. _Set up your Environment_

Make sure you have Python 3.8 or higher installed. You can check with:
```bash
python --version
```

3. _Install Required Packages_

BudgetBuddy uses `matplotlib` for chart generation.You can install dependencies with:
```bash
pip install matplotlib
```

4. _Run the App_

Navigate to the scripts folder and launch the main script:
```bash
cd scripts
python main.py
```

**Notes**

- Budget summaries will be saved in the `csv_reports/` folder.
- Progress charts will be saved in the `charts/` folder.
- These folders exist or will be created automatically when you run the app.
---

### ✨Usage

1.  _Launch the App_

 After navigating to the `scripts` folder, run the main script:
 ```bash
 python main.py
 ```
 The welcome message and a random financial quote will be displayed if the app ran successfully.

![Welcome Message](Screenshots/welcome_message.png)
*A warm greeting to kick off your budgeting journey.*

2. _Enter Your Financial details_

Follow the on-screen instructions to input your financial details.
![Inputs](Screenshots/inputs.png)
*Simple, guided input for a smooth start.*

Once submitted, a summary will be displayed on the terminal.
![Budget Summary](Screenshots/budget_summary.png)
*Your financial snapshot, clearly laid out*

3. _Saving Suggestions_

You will receive either an auto-suggested savings amount or a flexible plan.
![Savings](Screenshots/savings_logic.png)
*Smart suggestions tailored to your budget.*

4. _Income Breakdown_

BudgetBuddy provides a detailed view of your income distribution in the terminal and as a saved PNG chart.
![Income Distribution](Screenshots/Income_distribution.png)
*See where your money goes.*

![Barchart](Screenshots/barchart.png)
*Visual insights to support smarter decisions.*

5. _Saving Your Budget_

Your budget summary will be saved in the `csv_reports` folder for future reference.
![Saving The File](Screenshots/file_saving.png)
*Your data, safely stored.*

Here is a sample of the output CSV file:
![CSV File Example](Screenshots/csv_sample_file.png)
*Clean, organized, and easy to review.*

6. _Predict Annual Savings_

Once you have saved at least three budget files, you can run the annual savings predictor to estimate your yearly savings.
```bash
python predict_savings.py
```
The app will analyze your saved data and generate a prediction based on your financial history.
![Loading files](Screenshots/loading_files.png)
*Reviewing your progress...*

![Annual Savings](Screenshots/annual_savings.png)
*Your future savings, visualized.*

---
### ✨Technologies Used
BudgetBuddy is built with simplicity and clarity in mind, using:

- **Python 3.8+** - Core language for logic, input handling, and file operations.
- **Matplotlib** - For generating income distribution charts.
- **OS and CSV modules** - For file management and data storage.
- **Modular Design** - Organized scripts for maintainability and scalability.
---

### ✨Contributing

Contributions are welcome and appreciated!
If you would like to improve BudgetBuddy, you can fork this repository and create a new branch to make your changes.
Please ensure your code is clean, modular, and well-documented. 

Feel free to reach out with ideas, feedback, or questions- Let's build something empowering together!

---

> “Empower users. Celebrate progress. Code with heart.” ✨

Made with ❤️ by Elma
