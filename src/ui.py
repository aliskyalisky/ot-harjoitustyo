from budget_service import Budget
from user import User
from user_service import UserService


class UI:
    def __init__(self, budget: Budget, user_service: UserService):
        self.budget = budget
        self.user_service = user_service
        self.logged_in = False

    def run(self):
        print("Welcome to Budgetor!")

        if self.logged_in:
            while True:
                print(
                    "1: add expense \n 2: edit income \n 3: list expenses \n 4: budget balance \n 5: exit \n 6: log out")
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
                        self.logged_in = False
                        break
                    case "6":
                        self.logged_in = False
                        print("Logged out")
                        break
        else: 
            while True:
                print(
                    "1: log in \n 2: register")
                command = input()

                match command:
                    case "1":
                        username = input("Enter username: ")
                        password = input("Enter password: ")
                        if self.user_service.check_login(username, password):
                            self.logged_in = True
                            print("login successful!")
                            break
                        else:
                            print("invalid credientials")
                    case "2":
                        username = input("Enter username: ")
                        password = input("Enter password: ")
                        new_user = User(username, password)
                        self.user_service.add_user(new_user)
                        print("registered successfully")

        if self.logged_in:
            self.run()
        