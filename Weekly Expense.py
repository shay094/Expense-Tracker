class Expense:
    def __init__(self, date, description, amount, budget, category):
        self.date = date
        self.description = description
        self.amount = amount
        self.budget = budget
        self.category = category  
        self.remaining_budget = budget - amount

class ExpenseTracker:
    def __init__(self):
        self.expenses = []
        self.total_budget = 1000 
        self.remaining_budget = self.total_budget

    def add_expense(self, expense):
        self.expenses.append(expense)
        self.update_remaining_budget()

    def remove_expense(self, index):
        if 0 <= index < len(self.expenses):
            removed_expense = self.expenses.pop(index)
            print(f"Removed expense: {removed_expense.description}")
            self.update_remaining_budget()
        else:
            print("Invalid expense index.")

    def view_expenses(self):
        if not self.expenses:
            print("No expenses to show.")
        else:
            print("Expense List:")
            for i, expense in enumerate(self.expenses, start=1):
                print(f"{i}. Date: {expense.date}, Description: {expense.description}, Amount: Ksh {expense.amount:.2f}, Category: {expense.category}, Remaining Budget: Ksh {expense.remaining_budget:.2f}")

    def update_remaining_budget(self):
        total_spent = sum(expense.amount for expense in self.expenses)
        self.remaining_budget = self.total_budget - total_spent

    def check_budget_alert(self):
        if self.remaining_budget < 0.2 * self.total_budget:
            print("Alert: Your remaining budget is below 20%!")

    def weekly_budget_reset(self):
        self.expenses = []
        self.remaining_budget = self.total_budget
        print("Weekly budget has been reset.")

    def generate_summary(self):
        print("Summary Report:")
        print(f"Total Budget: Ksh {self.total_budget:.2f}")
        print(f"Remaining Budget: Ksh {self.remaining_budget:.2f}")
        total_spent = sum(expense.amount for expense in self.expenses)
        print(f"Total Spent: Ksh {total_spent:.2f}")
        if self.expenses:
            most_expensive = max(self.expenses, key=lambda x: x.amount)
            print(f"Most Expensive Item: {most_expensive.description} (Ksh {most_expensive.amount:.2f})")

    def save_to_file(self, filename):
        data = {
            "total_budget": self.total_budget,
            "remaining_budget": self.remaining_budget,
            "expenses": [
                {
                    "date": expense.date,
                    "description": expense.description,
                    "amount": expense.amount,
                    "category": expense.category
                } for expense in self.expenses
            ]
        }
        with open(filename, 'w') as file:
            json.dump(data, file)
        print("Data saved successfully.")

    def load_from_file(self, filename):
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
                self.total_budget = data["total_budget"]
                self.remaining_budget = data["remaining_budget"]
                self.expenses = [
                    Expense(exp["date"], exp["description"], exp["amount"], self.total_budget, exp["category"])
                    for exp in data["expenses"]
                ]
            print("Data loaded successfully.")
        except FileNotFoundError:
            print("File not found. Starting with an empty tracker.")

import json

def main():
    tracker = ExpenseTracker()

    while True:
        print("\nExpense Tracker")
        print("1. Add expense")
        print("2. Remove expense")
        print("3. View expenses")
        print("4. Check budget alert")
        print("5. Weekly budget reset")
        print("6. Generate summary report")
        print("7. Save to file")
        print("8. Load from file")
        print("9. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            date = input("Enter the date (YYYY-MM-DD): ")
            description = input("Enter the description: ")
            amount = float(input("Enter the amount: "))
            category = input("Enter the category: ")
            expense = Expense(date, description, amount, tracker.total_budget, category)
            tracker.add_expense(expense)
        elif choice == "2":
            index = int(input("Enter the index of the expense to remove: ")) - 1
            tracker.remove_expense(index)
        elif choice == "3":
            tracker.view_expenses()
        elif choice == "4":
            tracker.check_budget_alert()
        elif choice == "5":
            tracker.weekly_budget_reset()
        elif choice == "6":
            tracker.generate_summary()
        elif choice == "7":
            filename = input("Enter the filename to save data: ")
            tracker.save_to_file(filename)
        elif choice == "8":
            filename = input("Enter the filename to load data: ")
            tracker.load_from_file(filename)
        elif choice == "9":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
