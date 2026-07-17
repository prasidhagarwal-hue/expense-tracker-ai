import csv
import os
from transaction import Transaction
class ExpenseTracker:
    def __init__(self):
        self.filename = "expenses.csv"
        self.transactions = self.load_transactions()
    
    def load_transactions(self):
        if not os.path.exists(self.filename):
            return []
        with open(self.filename , "r") as file:
            reader = csv.DictReader(file)
            transactions = []
            for row in reader:
             t = [Transaction(row["amount"], row["category"], row["type"], row["note"]) for row in reader]
             t.date = row["date"]
             transactions.append(t)
            return transactions
    
    def save_transactions(self):
        with open(self.filename, "w", newline = "") as file:
             fieldnames = ["amount", "category", "trans_type", "date", "note"]
             writer = csv.DictWriter(file, fieldnames=fieldnames)
             writer.writeheader()
             for t in self.transactions:
                 writer.writerow(t.to_dict())
    
    def add_expense(self, amount, category, note = ""):
        transaction = Transaction(amount, category, "expense", note)
        self.transactions.append(transaction)
        self.save_transactions()
        print("Expense added")
    
    def add_income(self, amount, category, note=""):
        transaction = Transaction(amount, category,"income" , note)
        self.transactions.append(transaction)
        self.save_transactions()
        print("Income added ")
