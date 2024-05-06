class Budget:
    """Luokka joka huolehtii budjetista
    """
    def __init__(self):
        self.expenses = {}
        self.income = 0

    def add_expense(self, name, amount):
        """Menon lisääminen

        Args:
            name : Menon nimi
            amount : Menon suuruus
        """
        self.expenses[name] = int(amount)

    def edit_income(self, amount):
        """Tulojen muokkaus

        Args:
            amount : Tulojen uusi määrä
        """
        self.income = int(amount)

    def balance(self):
        """Laskee budjetin kokonaissaldon

        Returns:
            int: tulot - menot
        """
        expenses = 0
        for expense in self.expenses: # pylint: disable=consider-using-dict-items
            expenses += self.expenses[expense]
        return self.income - expenses

    def future_balance(self, months):
        """Laskee budjetin tulevaisuuden kokonaissaldon

        Returns:
            int: tulot - menot
        """
        return self.balance() * int(months)

    def list_expenses(self):
        """Listaa kaikki menot

        Returns:
            str: Tekstimuotoinen lista menoista
        """
        text = ""
        for expense in self.expenses: # pylint: disable=consider-using-dict-items
            text += str(expense) + ": " + str(self.expenses[expense]) + "\n"
        return text
