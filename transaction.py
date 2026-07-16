from datetime import date

class Transaction:
    def __init__(self, amount, category, trans_type, note=""):
        self.amount     = float(amount)
        self.category   = category
        self.trans_type = trans_type  
        self.date       = str(date.today()) 
        self.note       = note

    def to_dict(self):
        return {
            "amount"   : self.amount,
            "category" : self.category,
            "type"     : self.trans_type,
            "date"     : self.date,
            "note"     : self.note
        }

    def __str__(self):
        return f"{self.date} | {self.trans_type.upper()} | {self.category} | ₹{self.amount} | {self.note}"