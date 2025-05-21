import datetime

expenses = []

def add_expense():
    date = input("Enter date (YYYY-MM-DD): ")
    category = input("Enter category: ")
    amount = float(input("Enter amount: "))
    description = input("Enter description: ")
    expenses.append({"date": date, "category": category, "amount": amount, "description": description})
    print("Expense added successfully.\n")

def view_expenses():
    if not expenses:
        print("No expenses recorded.\n")
    else:
        for i, e in enumerate(expenses, start=1):
            print(f"{i}. {e['date']} | {e['category']} | ${e['amount']} | {e['description']}")

def total_by_category():
    category = input("Enter category: ")
    total = sum(e['amount'] for e in expenses if e['category'].lower() == category.lower())
    print(f"Total for {category}: ${total:.2f}\n")

def delete_expense():
    view_expenses()
    idx = int(input("Enter expense number to delete: ")) - 1
    if 0 <= idx < len(expenses):
        del expenses[idx]
        print("Deleted successfully.\n")
    else:
        print("Invalid entry.\n")

def main():
    while True:
        print("1. Add Expense\n2. View All\n3. Total by Category\n4. Delete Expense\n5. Exit")
        choice = input("Choose: ")
        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            total_by_category()
        elif choice == '4':
            delete_expense()
        elif choice == '5':
            break
        else:
            print("Invalid choice.\n")

main()
