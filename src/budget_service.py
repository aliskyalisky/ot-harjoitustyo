class Budget:
    def __init__(self):
        self.expenses = {}
        self.income = 0

    def add_expense(self, name, amount):
        self.expenses[name] = int(amount)

    def edit_income(self, amount):
        self.income = int(amount)

    def balance(self):
        expenses = 0
        for expense in self.expenses:
            expenses += self.expenses[expense]
        return self.income - expenses

    def list_expenses(self):
        text = ""
        for expense in self.expenses:
            text += str(expense) + ": " + str(self.expenses[expense]) + "\n"
        return text
            