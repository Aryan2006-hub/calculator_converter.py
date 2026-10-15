
import csv
import os
from datetime import date

FILE = "expenses.csv"
FIELDS = ["date", "category", "description", "amount"]


def initialize_file():
    if not os.path.exists(FILE):
        with open(FILE, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=FIELDS)
            writer.writeheader()


def add_expense():
    category = input("Enter category: ").strip()
    description = input("Enter description: ").strip()

    if not category or not description:
        print("Category and description cannot be empty!")
        return

    while True:
        try:
            amount = float(input("Enter amount: "))
            if amount <= 0:
                print("Amount must be positive!")
                continue
            break
        except ValueError:
            print("Please enter a valid amount!")

    expense_date = input(
        "Enter date (YYYY-MM-DD) or press Enter for today: "
    ).strip()

    if not expense_date:
        expense_date = date.today().isoformat()
    else:
        try:
            date.fromisoformat(expense_date)
        except ValueError:
            print("Invalid date! Using today's date.")
            expense_date = date.today().isoformat()

    with open(FILE, "a", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS)
        writer.writerow({
            "date": expense_date,
            "category": category,
            "description": description,
            "amount": f"{amount:.2f}"
        })

    print("Expense saved successfully!")


def read_expenses():
    with open(FILE, "r", newline="") as f:
        return list(csv.DictReader(f))


def view_expenses(expenses=None):
    if expenses is None:
        expenses = read_expenses()

    if not expenses:
        print("No expenses found.")
        return

    print("\nDate | Category | Description | Amount")
    print("-" * 50)

    for e in expenses:
        print(
            e["date"], "|", e["category"], "|",
            e["description"], "| ₹", e["amount"]
        )


def filter_expenses():
    category = input("Enter category to filter: ").strip().lower()

    expenses = [
        e for e in read_expenses()
        if e["category"].lower() == category
    ]

    view_expenses(expenses)


def category_summary():
    expenses = read_expenses()
    totals = {}

    for e in expenses:
        category = e["category"]
        totals[category] = totals.get(category, 0) + float(e["amount"])

    if not totals:
        print("No expenses available.")
        return

    print("\nCategory-wise Summary:")
    for category, total in totals.items():
        print(f"{category}: ₹{total:.2f}")

    print(f"Total Expenses: ₹{sum(totals.values()):.2f}")


initialize_file()

while True:
    print("\n--- Personal Expense Tracker ---")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. Filter by Category")
    print("4. Category Summary")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        filter_expenses()
    elif choice == "4":
        category_summary()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice! Try again.")
