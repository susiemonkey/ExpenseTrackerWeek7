import requests

class ExpenseTracker:
    API_URL = "https://api.example.com/expenses"  # Placeholder API URL

    def add_expense(self, description, amount, date):
        data = {"description": description, "amount": amount, "date": date}
        response = requests.post(self.API_URL, json=data)
        return response.json()

    def view_expenses(self):
        response = requests.get(self.API_URL)
        return response.json()

    def update_expense(self, expense_id, description=None, amount=None, date=None):
        data = {"description": description, "amount": amount, "date": date}
        response = requests.put(f"{self.API_URL}/{expense_id}", json=data)
        return response.json()

    def delete_expense(self, expense_id):
        response = requests.delete(f"{self.API_URL}/{expense_id}")
        return response.status_code == 204
