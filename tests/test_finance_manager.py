import os
from finance_manager import FinanceManager

class TestFinanceManager(unittest.TestCase):
    def setUp(self):
        """Setup a temporary finance manager before each test."""
        self.filename = "test_data.json"  # Use a separate file for testing
        # Ensure any existing test data file is removed before each test
        if os.path.exists(self.filename):
            os.remove(self.filename)
        self.fm = FinanceManager("TestUser", filename=self.filename)

    def tearDown(self):
        """Clean up after tests."""
        if os.path.exists(self.filename):
            os.remove(self.filename)
    def test_add_expense(self):
        """Test adding an expense."""
        self.fm.add_expense(100, "Groceries")
        self.assertEqual(len(self.fm._user_data['expenses']), 1)
        self.assertEqual(self.fm._user_data['expenses'][0]['amount'], 100)
        self.assertEqual(self.fm._user_data['expenses'][0]['category'], "Groceries")

    def test_add_income(self):
        """Test adding an income."""
        self.fm.add_income(500, "Salary")
        self.assertEqual(len(self.fm._user_data['income']), 1)
        self.assertEqual(self.fm._user_data['income'][0]['amount'], 500)
        self.assertEqual(self.fm._user_data['income'][0]['source'], "Salary")

if __name__ == '__main__':
    unittest.main()
