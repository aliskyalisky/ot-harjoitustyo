from budget_service import Budget

class UI:
    def __init__(self, budget: Budget):
        self.budget = budget

    def run(self):
        print("Welcome to Budgetor!")
        while True:
            print("1: add expense \n 2: edit income \n 3: list expenses \n 4: budget balance \n 5: exit")
            command = input()

            match command:
                case "1":
                    name = input("Expense name ")
                    amount = input("Expense amount ")
                    self.budget.add_expense(name, amount)
                    print("Expense added!")
                case "2":
                    print(f"current income: {self.budget.income}")
                    new_income = input("Enter your income ")
                    self.budget.edit_income(new_income)
                    print("Income edited!")
                case "3":
                    print(self.budget.list_expenses())
                case "4":
                    print(f"Current balance: {self.budget.balance()}")
                case "5":
                    print("Thank you for using Budgetor!")
                    break
