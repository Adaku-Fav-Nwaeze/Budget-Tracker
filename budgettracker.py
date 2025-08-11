expenses = []

def add_expenses():
    category = input("Enter category: ")
    try:
        amount = float(input("Enter the amount: "))
        expense = {"category": category, "amount": amount}
        expenses.append(expense)
        print("Expense added")
    except ValueError:
        print("The amount you entered is an invalid amount, try again")

def view_expenses():
    if not expenses:
        print("No expenses found or recorded yet")
        return
    print("\nAll expenses")
    for i, expense in enumerate(expenses):
        num = i + 1
        category = expense['category']
        amount = expense['amount']
        print(f"{num}. {category} - {amount}")

def update_expenses():
    view_expenses()
    if not expenses:
        return
    try:
        index = int(input("Enter number of expense to update: ")) - 1
        if 0 <= index < len(expenses):
            category = input("New category: ")
            amount = float(input("New amount: "))
            expenses[index] = {"category": category, "amount": amount}
            print("Expense updated.")
        else:
            print("Invalid number.")
    except ValueError:
        print("Please enter a valid number.")

def delete_expense():
    view_expenses()
    if not expenses:
        return
    try:
        index = int(input("Enter number of expense to delete: ")) - 1
        if 0 <= index < len(expenses):
            removed = expenses.pop(index)
            print(f"Removed: {removed['category']} - {removed['amount']}")
        else:
            print("Invalid number.")
    except ValueError:
        print("Please enter a valid number.")

def view_total():
    total = sum(exp["amount"] for exp in expenses)
    print(f"\nTotal Expenses: {total}")

def save_to_file():
    with open("budget.txt", "w") as file:
        for expense in expenses:
            file.write(f"{expense['category']} - {expense['amount']}\n")
    print("Expenses saved to 'budget.txt'.")

def budget_tracker():
    while True:
        print("\n   BUDGET TRACKER MENU")
        print("1. Add Expense")
        print("2. View Expense")
        print("3. Update Expense")
        print("4. Delete Expense")
        print("5. View Total")
        print("6. Save to File")
        print("7. Exit")

        choice = input("Choose an option from 1 - 7: ")
        if choice == "1":
            add_expenses()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            update_expenses()
        elif choice == "4":
            delete_expense()
        elif choice == "5":
            view_total()
        elif choice == "6":
            save_to_file()
        elif choice == "7":
            print("Have a nice time")
            break
        else:
            print("You entered an invalid option")

budget_tracker()
