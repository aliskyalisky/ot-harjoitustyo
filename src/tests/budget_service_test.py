import unittest
from budget_service import Budget

class TestBudget(unittest.TestCase):
    def setUp(self):
        pass

    def test_income_updates(self):
        budget = Budget()
        budget.edit_income(1000)

        self.assertEqual(budget.income, 1000)