import os
import json

def load_data(filename="budget_data.json"):
    """Load budget data from a file."""
    if not os.path.exists(filename):
        return {"transactions": []}
    with open(filename, "r") as file:
        return json.load(file)

def save_data(data, filename="budget_data.json"):
    """Save budget data to a file."""
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)

def add_transaction(data, amount, category, transaction_type):
    """Add an income or expense transaction."""
    data["transactions"].append({
        "amount": amount,
        "category": category,
        "type": transaction_type
    })
    save_data(data)
    print("Transaction added successfully!")

def calculate_balance(data):
    """Calculate the total balance."""
    income = sum(t["amount"] for t in data["transactions"] if t["type"] == "income")
    expenses = sum(t["amount"] for t in data["transactions"] if t["type"] == "expense")
    return income - expenses

def generate_report(data):
    """Generate a summary report."""
    print("\nBudget Report")
    print("=" * 20)
    for t in data["transactions"]:
        print(f"{t['type'].capitalize()}: {t['amount']} - {t['category']}")
    print("=" * 20)
    print(f"Total Balance: {calculate_balance(data)}")

def main():
    data = load_data()
    while True:
        print("\nBudget Tracker Menu:")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View Report")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            amount = float(input("Enter income amount: "))
            category = input("Enter income category: ")
            add_transaction(data, amount, category, "income")
        
        elif choice == "2":
            amount = float(input("Enter expense amount: "))
            category = input("Enter expense category: ")
            add_transaction(data, amount, category, "expense")
        
        elif choice == "3":
            generate_report(data)
        
        elif choice == "4":
            print("Exiting Budget Tracker. Have a great day!")
            break
        
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()