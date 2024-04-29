import unittest
from budget_service import Budget


class TestBudget(unittest.TestCase):
    def setUp(self):
        pass

    def test_income_updates(self):
        budget = Budget()
        budget.edit_income(1000)

        self.assertEqual(budget.income, 1000)

    def test_balance_is_correct(self):
        budget = Budget()
        budget.edit_income(1000)
        budget.add_expense("food", 200)

        self.assertEqual(budget.balance(), 800)