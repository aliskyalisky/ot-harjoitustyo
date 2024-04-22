from budget_service import Budget
from user_service import UserService
from ui import UI

budget = Budget()
userservice = UserService()
ui = UI(budget, userservice)
ui.run()
