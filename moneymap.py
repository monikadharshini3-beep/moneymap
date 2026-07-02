# =========================================
#         MONEYMAP BUDGET TRACKER
# =========================================

# ---------- USER CLASS ----------
class User:
    def __init__(self):
        self.username = "admin"
        self.password = "1234"

    def login(self):
        print("\n========== LOGIN ==========")
        user = input("Enter Username : ")
        pwd = input("Enter Password : ")

        if user == self.username and pwd == self.password:
            print("\nLogin Successful!\n")
            return True
        else:
            print("\nInvalid Username or Password")
            return False

    def report(self):
        print("General Report")


# ---------- MONEYMAP CLASS ----------
class MoneyMap(User):
    def __init__(self):
        super().__init__()
        # Encapsulation
        self.__salary = 0
        self.__bill = 0
        self.__goal = 0
        # Data Arrays
        self.categories = []
        self.amounts = []
        self.expense_items = []
        self.expense_costs = []

    # ---------- SETTERS ----------
    def set_salary(self, salary):
        self.__salary = salary

    def set_bill(self, bill):
        self.__bill = bill

    def set_goal(self, goal):
        self.__goal = goal

    # ---------- GETTERS ----------
    def get_salary(self):
        return self.__salary

    def get_bill(self):
        return self.__bill

    def get_goal(self):
        return self.__goal

    # Dynamic limits engine
    def calculate_limits(self, category_name):
        cat = category_name.lower()
        salary = self.get_salary()
        
        if salary <= 15000:
            if cat == "food": 
                return salary * 0.10, salary * 0.20
            elif cat == "shopping": 
                return salary * 0.05, salary * 0.10
            elif cat == "travel": 
                return salary * 0.05, salary * 0.10
            else: 
                return salary * 0.05, salary * 0.10
        else:
            if cat == "food": 
                return salary * 0.40, salary * 0.50
            elif cat == "shopping": 
                return salary * 0.10, salary * 0.20
            elif cat == "travel": 
                return salary * 0.10, salary * 0.15
            else: 
                return salary * 0.10, salary * 0.15

    # ---------- CHOICE 1 ----------
    def blueprint(self):
        print("\n================================")
        print("        BASIC DETAILS")
        print("================================")
        self.set_salary(int(input("Enter Salary : ₹")))
        bill = input("Do you have Bills? (yes/no) : ").lower()

        if bill == "yes":
            self.set_bill(int(input("Enter Bill Amount : ₹")))
        else:
            self.set_bill(0)

        self.set_goal(int(input("Enter Saving Goal : ₹")))

        print("\n================================")
        print("        BUDGET PLAN")
        print("================================")
        n = int(input("How many Categories? "))

        self.categories = []
        self.amounts = []
        for i in range(n):
            category = input("\nEnter Category : ")
            amount = int(input("Enter Budget Amount : ₹"))

            minimum, maximum = self.calculate_limits(category)
            print("Recommended Budget : ₹", int(minimum), "to ₹", int(maximum))

            if amount > maximum:
                print("⚠ Budget exceeds safety threshold limits.")
                amount = int(input("Enter Correct Budget : ₹"))

            self.categories.append(category)
            self.amounts.append(amount)

    # ---------- CHOICE 2 ----------
    def report(self):
        print("\n====================================")
        print("         BUDGET SUMMARY")
        print("====================================")
        print("Salary        : ₹", self.get_salary())
        print("Bills         : ₹", self.get_bill())
        print("Saving Goal   : ₹", self.get_goal())

        print("\n------------ BUDGET PLAN DETAILS ------------")
        total_budget = 0
        for i in range(len(self.categories)):
            category = self.categories[i]
            spent = self.amounts[i]
            minimum, maximum = self.calculate_limits(category)

            print(f"\nCategory : {category}")
            print(f"Budget   : ₹{spent}")
            print(f"Recommended Range : ₹{int(minimum)} to ₹{int(maximum)}")

            if spent > maximum:
                print("⚠ Reduce planned variance allocations by ₹", int(spent - maximum))
            else:
                print("✅ Good Allocation Strategy")
            total_budget += spent

        print("\n------------ ACTUAL SPENDING DAILY LOG ------------")
        total_daily_spent = sum(self.expense_costs)
        if not self.expense_items:
            print("No daily expenses tracked yet in current logs.")
        else:
            for idx in range(len(self.expense_items)):
                print(f"- {self.expense_items[idx]} : ₹{self.expense_costs[idx]}")
            print("Total Logged Daily Expenses : ₹", total_daily_spent)

        print("----------------------------------------")
        print("Total Planned Budget Target : ₹", total_budget)
        total_expense = total_budget + self.get_bill() + total_daily_spent
        print("Total Combined Outflow      : ₹", total_expense)

        balance = self.get_salary() - total_expense
        print("Remaining Asset Runway      : ₹", balance)
        print("----------------------------------------")

        if balance >= self.get_goal():
            print("🎯 Saving Goal Achieved")
            print("Emergency Reserve Buffer Available : ₹", balance - self.get_goal())
        else:
            print("⚠ Saving Goal Deficit Notice")
            print("Need ₹", self.get_goal() - balance, "more to cover margins.")
        print("====================================")

    # ---------- CHOICE 3 ----------
    def tracker(self):
        while True:
            print("\n====================================")
            print("      DAILY EXPENSE TRACKER")
            print("====================================")
            print("1. Log an Expense")
            print("2. View Logged Expenses")
            print("3. Back to Main Menu")
            print("====================================")
            sub_choice = input("Enter Tracker Choice: ")
            
            if sub_choice == "1":
                item = input("What did you buy? / Expense Name: ").strip()
                cost = int(input("Enter Expense Amount : ₹"))
                self.expense_items.append(item)
                self.expense_costs.append(cost)
                print(f"✅ Success! Logged ₹{cost} to ledger database stack.")
            elif sub_choice == "2":
                print("\n--- Current Workspace Ledger Logs ---")
                if not self.expense_items:
                    print("Empty profile ledger record instances detected.")
                else:
                    for i in range(len(self.expense_items)):
                        print(f"• {self.expense_items[i]} : ₹{self.expense_costs[i]}")
                    print("Sum Total Cost Outflow: ₹", sum(self.expense_costs))
            elif sub_choice == "3":
                break
            else:
                print("Invalid operational choice direction. Retry.")


# ===============================
# MAIN RUNTIME PIPELINE EXECUTION
# ===============================
money = MoneyMap()

if money.login():
    while True:
        print("\n====================================")
        print("           MONEYMAP")
        print("====================================")
        print("1. Basic Details & Budget Plan")
        print("2. Budget Summary")
        print("3. Daily Expense Tracker")
        print("4. Exit")
        print("====================================")

        choice = input("Enter Choice : ")
        if choice == "1":   
            money.blueprint()
        elif choice == "2": 
            money.report()
        elif choice == "3": 
            money.tracker()
        elif choice == "4":
            print("\nThank you for tracking with MoneyMap! 😊")
            break
        else:
            print("Invalid Action Selected.")