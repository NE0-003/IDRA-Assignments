import csv
import os

file_name = "expenses.csv"

def create_file():
    if not os.path.exists(file_name):
        with open(file_name, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Category", "Amount", "Note"])

def add_expense():
    date = input("Enter Date: ")
    category = input("Enter Category: ")

    try:
        amount = float(input("Enter Amount: "))
    except:
        print("Invalid amount")
        return

    note = input("Enter Note (optional): ")

    with open(file_name, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount, note])

    print("Expense added")

def view_expenses():
    total = 0

    with open(file_name, "r") as file:
        reader = csv.reader(file)
        next(reader)

        print("\nDate\tCategory\tAmount\tNote")
        for row in reader:
            print(row[0], "\t", row[1], "\t", row[2], "\t", row[3])
            total += float(row[2])

    print("Total Amount Spent:", total)

def category_summary():
    summary = {}

    with open(file_name, "r") as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            category = row[1]
            amount = float(row[2])

            if category in summary:
                summary[category] += amount
            else:
                summary[category] = amount

    print("\nCategory Wise Spending")
    for category in summary:
        print(category, ":", summary[category])

create_file()

while True:
    print("\n1. Add Expense")
    print("2. View Expenses")
    print("3. Category Summary")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        try:
            view_expenses()
        except:
            print("No expenses found")
    elif choice == "3":
        try:
            category_summary()
        except:
            print("No expenses found")
    elif choice == "4":
        print("Thank you")
        break
    else:
        print("Invalid choice")