from data_manager import save_data, load_data

class FinanceManager:
    def __init__(self, user_name, filename="data.json"):
        self.user_name = user_name
        self.filename = filename
        self._user_data = load_data(self.filename)
        if not self._user_data:
            self._user_data = {'expenses': [], 'income': [], 'investments': {}, 'goals': []}

    def add_expense(self, amount, category):
        self._user_data['expenses'].append({'amount': amount, 'category': category})
        self._save_data()

    def add_income(self, amount, source):
        self._user_data['income'].append({'amount': amount, 'source': source})
        self._save_data()

    def add_investment(self, name, quantity, purchase_price, current_price=None):
        self._user_data['investments'][name] = {
            'quantity': quantity, 'purchase_price': purchase_price, 'current_price': current_price}
        self._save_data()

    def set_financial_goal(self, goal, target_amount):
        self._user_data['goals'].append({'goal': goal, 'target_amount': target_amount, 'progress': 0})
        self._save_data()

    def update_goal_progress(self, goal, progress):
        for g in self._user_data['goals']:
            if g['goal'] == goal:
                g['progress'] += progress
                break
        self._save_data()

    def view_financial_summary(self):
        print("\nFinancial Summary:")
        total_expenses = sum(expense['amount'] for expense in self._user_data['expenses'])
        print(f"Total Expenses: ${total_expenses:.2f}")
        if self._user_data['expenses']:
            print("Expenses by Category:")
            for expense in self._user_data['expenses']:
                print(f" - {expense['category'].title()}: ${expense['amount']:.2f}")

        total_income = sum(income['amount'] for income in self._user_data['income'])
        print(f"\nTotal Income: ${total_income:.2f}")
        if self._user_data['income']:
            print("Income Sources:")
            for income in self._user_data['income']:
                print(f" - {income['source'].title()}: ${income['amount']:.2f}")

        if self._user_data['investments']:
            print("\nInvestments:")
            for name, details in self._user_data['investments'].items():
                current_value = details['quantity'] * (details.get('current_price') or details['purchase_price'])
                print(f" - {name.title()}: {details['quantity']} units at ${details['purchase_price']:.2f} each. Current value: ${current_value:.2f}")
        else:
            print("\nNo investments recorded.")

        if self._user_data['goals']:
            print("\nFinancial Goals:")
            for goal in self._user_data['goals']:
                print(f" - Goal: {goal['goal'].title()}, Target: ${goal['target_amount']:.2f}, Progress: ${goal['progress']:.2f}")
        else:
            print("\nNo financial goals set.")

    def _save_data(self):
        save_data(self._user_data, self.filename)
