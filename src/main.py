from finance_manager import FinanceManager

def main_menu():
    fm = FinanceManager("User")  # You might want to implement user name input in future

    while True:
        print("\nWelcome to GoldFrog - Your Personal Finance Manager")
        print("1: Add Expense")
        print("2: Add Income")
        print("3: Add Investment")
        print("4: Set Financial Goal")
        print("5: View Financial Summary")
        print("6: Exit")
        choice = input("Please select an option: ")

        if choice == "6":
            print("Thank you for using GoldFrog. Goodbye!")
            break
        elif choice == "1":
            add_expense(fm)
        elif choice == "2":
            add_income(fm)
        elif choice == "3":
            add_investment(fm)
        elif choice == "4":
            set_financial_goal(fm)
        elif choice == "5":
            fm.view_financial_summary()
        else:
            print("Invalid option, please try again.")

def add_expense(fm):
    try:
        amount = float(input("Enter the expense amount: "))
        category = input("Enter the expense category: ")
        fm.add_expense(amount, category)
        print("Expense added successfully.")
    except ValueError:
        print("Invalid amount. Please enter a valid number.")

def add_income(fm):
    try:
        amount = float(input("Enter the income amount: "))
        source = input("Enter the income source: ")
        fm.add_income(amount, source)
        print("Income added successfully.")
    except ValueError:
        print("Invalid amount. Please enter a valid number.")

def add_investment(fm):
    try:
        name = input("Enter the investment name: ")
        quantity = int(input("Enter the quantity of the investment: "))
        purchase_price = float(input("Enter the purchase price per unit: "))
        # Optional: current price
        current_price = input("Enter the current price per unit (optional, press enter to skip): ")
        current_price = float(current_price) if current_price else None
        fm.add_investment(name, quantity, purchase_price, current_price)
        print("Investment added successfully.")
    except ValueError:
        print("Invalid input. Please enter valid numbers for quantity and prices.")

def set_financial_goal(fm):
    goal = input("Enter your financial goal (e.g., 'Save for a vacation'): ")
    try:
        target_amount = float(input("Enter the target amount for your goal: "))
        fm.set_financial_goal(goal, target_amount)
        print("Financial goal set successfully.")
    except ValueError:
        print("Invalid target amount. Please enter a valid number.")

if __name__ == "__main__":
    main_menu()
