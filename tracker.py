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
        with open(self.filename, "r") as f:
            reader = csv.DictReader(f)
            transactions = []
            for row in reader:
                t = Transaction(row["amount"], row["category"], row["trans_type"], row["note"])
                t.date = row["date"]
                transactions.append(t)
            
            return transactions
    
    def save_transactions(self):
        with open(self.filename, "w") as f:
            fieldnames = ["amount", "category", "trans_type" , "date", "note"]
            write = csv.DictWriter(f, fieldnames=fieldnames)
            write.writeheader()
            for t in self.transactions:
                write.writerow(t.to_dict())
    
    def add_expense(self,amount, category, note = ""):
        transaction = Transaction(amount, category, "expense", note)
        self.transactions.append(transaction)
        self.save_transactions()
        print("Expense added")
    
    def add_income(self,amount, category, note= ""):
        transaction = Transaction(amount, category, "income", note)
        self.transactions.append(transaction)
        self.save_transactions()
        print("Income added")
    
    def view_all(self):
        if not self.transactions:
            print("no transaction found")
        else:
            for transaction in self.transactions:
                print(transaction)
    
    def month_summary(self):
         total_expense = 0
         total_income = 0
         categories = {}
         for transaction in self.transactions:
             if transaction.trans_type == "income":
                 total_income += transaction.amount
             else:
                total_expense += transaction.amount
            
             category = transaction.category
             if category not in categories:
                 categories[category] = 0
             categories[category] += transaction.category

         balance = total_income - total_expense
         print("=====MONTHLY SUMMARY=====")
         print(f"Total Income = ₹{total_income}")
         print(f"Total expense = ₹{total_expense}")
         print(f"Balance = ₹{balance}")
         print(f"\n Category breakdown")
         for category, amount in categories.items():
             print(f"{category} :₹{amount}" )
         print("=================")               

 