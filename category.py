import matplotlib.pyplot as plt

class ExpenseTracker:
    def __init__(self):
        self.expenses = {
            "Housing": [],
            "Food": [],
            "Transportation": [],
            "Entertainment": [],
            "Miscellaneous": []
        }

    def add_expense(self, category, amount, description):
        self.expenses[category].append({"Amount": amount, "Description": description})

    def view_expenses(self):
        for category, expenses in self.expenses.items():
            print(f"{category} Expenses:")
            for expense in expenses:
                print(f"Amount: {expense['Amount']}, Description: {expense['Description']}")

    def total_spending(self):
        total = 0
        for expenses in self.expenses.values():
            for expense in expenses:
                total += expense["Amount"]
        return total

    def visualize_expenses(self):
        categories = list(self.expenses.keys())
        amounts = [sum(expense["Amount"] for expense in self.expenses[category]) for category in categories]

        plt.bar(categories, amounts)
        plt.xlabel("Category")
        plt.ylabel("Amount ($)")
        plt.title("Expense Distribution")
        plt.show()

def main():
    tracker = ExpenseTracker()
    while True:
        print("\n1. Add Expense\n2. View Expenses\n3. Total Spending\n4. Visualize Expenses\n5. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            category = input("Enter category (Housing, Food, Transportation, Entertainment, Miscellaneous): ")
            if category not in tracker.expenses:
                print("Invalid category. Please enter one of the predefined categories.")
                continue
            amount = input("Enter amount: ")
            try:
                amount = float(amount)
            except ValueError:
                print("Invalid amount. Please enter a numeric value.")
                continue
            description = input("Enter description: ")
            tracker.add_expense(category, amount, description)
        elif choice == "2":
            tracker.view_expenses()
        elif choice == "3":
            print(f"Total spending: ${tracker.total_spending():.2f}")
        elif choice == "4":
            tracker.visualize_expenses()
        elif choice == "5":
            break
        else:
            print("Invalid option")

if __name__ == "__main__":
    main()