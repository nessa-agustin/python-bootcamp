class CostTracker:
    def __init__(self):
        self.running = True
        self.expenses = []

    def spend(self):
        # self.expenses.append(amount)
        new_expense = float(input("Enter new expense: "))
        self.expenses.append(new_expense)
        print(f"Added PHP {new_expense} to expenses")

    def refund(self):
        # self.expenses.remove(amount)
        # self.expenses.pop(-1)
        if self.expenses:
            refunded = self.expenses.pop(-1)
            print(f"Refunded PHP {refunded}")
        else:
            print("No expenses yet")

    def show(self):
        print(f"Expenses: (total PHP{sum(self.expenses)})")
        for number, expense in enumerate(self.expenses, start=1):
            print(f"\tExpense {number}:\tPHP {expense}")

    def main_loop(self):
        # running = True
        # current_expenses = []

        while self.running:
            command = input("Command: ")

            # if command == 'exit':
            #     running = False
            #     break

            # if command != 'show':
            #     expense_amount = int(input('Enter amount: '))

            if command == "spend":
                self.spend()
            elif command == "refund":
                self.refund()
            elif command == "show":
                self.show()
            elif command == "exit":
                self.running = False


cost_tracker = CostTracker()
cost_tracker.main_loop()