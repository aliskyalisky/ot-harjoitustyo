import unittest
from user_service import UserService
from user import User


class TestBudget(unittest.TestCase):
    def setUp(self):
        pass

    def test_adding_user(self):
        user_service = UserService()
        new_user = User("Kalle", "Kalle123")
        user_service.add_user(new_user)
        self.assertEqual(len(user_service.list_users()), 1)

    def test_check_login_works(self):
        user_service = UserService()
        new_user = User("Kalle", "Kalle123")
        user_service.add_user(new_user)
        self.assertEqual(user_service.check_login("Kalle", "Kalle123"), True)