from tracker import ExpenseTracker

def main():
    tracker = ExpenseTracker()
    
    while True:
        print("\n====== EXPENSE TRACKER ======")
        print("1. Add expense")
        print("2. Add income")
        print("3. View all transactions")
        print("4. Monthly summary")
        print("5. Get AI advice")
        print("6. Exit")
        print("=============================")
        
        choice = input("Enter choice: ").strip()
        
        if choice == "1":
            amount   = input("Enter amount   : ").strip()
            category = input("Enter category (Food/Transport/Shopping/Other): ").strip()
            note     = input("Enter note (optional, press Enter to skip): ").strip()
            tracker.add_expense(amount, category, note)
            
        elif choice == "2":
            amount   = input("Enter amount   : ").strip()
            category = input("Enter category (Salary/Freelance/Other): ").strip()
            note     = input("Enter note (optional, press Enter to skip): ").strip()
            tracker.add_income(amount, category, note)
            
        elif choice == "3":
            tracker.view_all()
            
        elif choice == "4":
            tracker.monthly_summary()
            
        elif choice == "5":
            from ai_advisor import chat_with_advisor
            summary = f"""
        Total transactions : {len(tracker.transactions)}
        """
            chat_with_advisor(summary)
            
        elif choice == "6":
            print("bye!")
            break
            
        else:
            print("Invalid choice. Please enter 1-6.")

if __name__ == "__main__":
    main()