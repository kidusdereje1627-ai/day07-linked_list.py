class Account:
    def init(self, owner, number, balance=0):
        self.owner = owner
        self.number = number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"{amount} withdrawn successfully.")
        else:
            print("Insufficient balance.")

    def statement(self):
        print("=== Account ===")
        print(f"Owner   : {self.owner}")
        print(f"Number  : {self.number}")
        print(f"Balance : {self.balance}")


class SavingsAccount(Account):
    def init(self, owner, number, balance=0, rate=0.05):
        super().init(owner, number, balance)
        self.rate = rate

    def add_interest(self):
        self.deposit(self.balance * self.rate)

    def statement(self):
        print("=== Savings Account ===")
        print(f"Owner   : {self.owner}")
        print(f"Number  : {self.number}")
        print(f"Balance : {self.balance}")
        print(f"Rate    : {self.rate}")


class CurrentAccount(Account):
    def init(self, owner, number, balance=0, overdraft=1000):
        super().init(owner, number, balance)
        self.overdraft = overdraft

    def withdraw(self, amount):
        if self.balance - amount >= -self.overdraft:
            self.balance -= amount
            print(f"{amount} withdrawn successfully.")
        else:
            print("Overdraft limit exceeded.")

    def statement(self):
        print("=== Current Account ===")
        print(f"Owner      : {self.owner}")
        print(f"Number     : {self.number}")
        print(f"Balance    : {self.balance}")
        print(f"Overdraft  : {self.overdraft}")


# Create objects
acc1 = Account("Abel", "1001", 5000)

acc2 = SavingsAccount("Kidus", "1002", 10000, 0.10)
acc2.add_interest()

acc3 = CurrentAccount("Hana", "1003", 2000, 1500)
acc3.withdraw(3000)

# Polymorphism
accounts = [acc1, acc2, acc3]

for account in accounts:
    account.statement()
    print()