def add_expense(expenses):
    description = input("Enter expense description: ")
    while True:
        try:
            amount = float(input("Enter expense amount: "))
            if amount <= 0:
                print("Amount must be greater than 0.")
            else:
                expenses.append((description, amount))
                print("Expense added successfully.")
                break
        except ValueError:
            print("Invalid input. Please enter a valid amount.")

def display_expenses(expenses):
    print("List of expenses:")
    if not expenses:
        print("No expenses recorded.")
    else:
        for i, (description, amount) in enumerate(expenses, start=1):
            print(f"{i}. {description}: ${amount}")

def calculate_total(expenses):
    total = sum(amount for _, amount in expenses)
    print(f"Total expenses: ${total:.2f}")

def main():
    expenses = []
    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. Display Expenses")
        print("3. Calculate Total Expenses")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_expense(expenses)
        elif choice == '2':
            display_expenses(expenses)
        elif choice == '3':
            calculate_total(expenses)
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()

#https://www.youtube.com/watch?v=-adT3bRWchI&ab_channel=ShaunHalverson