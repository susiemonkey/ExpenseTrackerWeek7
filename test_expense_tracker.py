import unittest
from unittest.mock import patch
from expense_tracker import ExpenseTracker

class TestExpenseTracker(unittest.TestCase):

    def setUp(self):
        self.tracker = ExpenseTracker()
        self.sample_data = {
            "description": "Lunch",
            "amount": 10.5,
            "date": "2023-11-01"
        }

    @patch("expense_tracker.requests.post")
    def test_add_expense(self, mock_post):
        mock_post.return_value.json.return_value = self.sample_data
        response = self.tracker.add_expense("Lunch", 10.5, "2023-11-01")
        mock_post.assert_called_once_with("https://api.example.com/expenses", json=self.sample_data)
        self.assertEqual(response, self.sample_data)

    @patch("expense_tracker.requests.get")
    def test_view_expenses(self, mock_get):
        mock_get.return_value.json.return_value = [self.sample_data]
        response = self.tracker.view_expenses()
        mock_get.assert_called_once_with("https://api.example.com/expenses")
        self.assertEqual(response, [self.sample_data])

    @patch("expense_tracker.requests.put")
    def test_update_expense(self, mock_put):
        expense_id = 1
        updated_data = {"description": "Dinner", "amount": 15.0, "date": "2023-11-01"}
        mock_put.return_value.json.return_value = updated_data
        response = self.tracker.update_expense(expense_id, "Dinner", 15.0, "2023-11-01")
        mock_put.assert_called_once_with("https://api.example.com/expenses/1", json=updated_data)
        self.assertEqual(response, updated_data)

    @patch("expense_tracker.requests.delete")
    def test_delete_expense(self, mock_delete):
        expense_id = 1
        mock_delete.return_value.status_code = 204
        response = self.tracker.delete_expense(expense_id)
        mock_delete.assert_called_once_with("https://api.example.com/expenses/1")
        self.assertTrue(response)
