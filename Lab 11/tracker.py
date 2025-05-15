expenses = []

def add_expense():
    date = input("Enter date (YYYY-MM-DD): ")
    category = input("Enter category: ")
    amount = float(input("Enter amount: "))
    description = input("Enter description: ")
    expenses.append({"date": date, "category": category, "amount": amount, "description": description})
    print("Expense added.\n")

def view_expenses():
    print("\n--- All Expenses ---")
    for i, exp in enumerate(expenses):
        print(f"{i+1}. {exp['date']} | {exp['category']} | ${exp['amount']} | {exp['description']}")
    print()

def total_by_category():
    cat = input("Enter category to sum: ")
    total = sum(exp['amount'] for exp in expenses if exp['category'].lower() == cat.lower())
    print(f"Total spent in '{cat}': ${total:.2f}\n")

def delete_expense():
    view_expenses()
    num = int(input("Enter expense number to delete: "))
    if 0 < num <= len(expenses):
        del expenses[num-1]
        print("Expense deleted.\n")
    else:
        print("Invalid entry.\n")

def main():
    while True:
        print("1. Add Expense\n2. View Expenses\n3. Total by Category\n4. Delete Expense\n5. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            total_by_category()
        elif choice == '4':
            delete_expense()
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.\n")

main()
