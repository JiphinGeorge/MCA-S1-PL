# Create a Bank account with members: account number, name, type of account and balance.
# Write constructor and methods to deposit and withdraw an amount.

class Bank:
    def __init__(self, acc_no, name, acc_type, balance):
        self.acc_no = acc_no
        self.name = name
        self.acc_type = acc_type
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Amount Deposited. New Balance:", self.balance)

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient Balance")
        else:
            self.balance -= amount
            print("Amount Withdrawn. New Balance:", self.balance)

# Example
b = Bank(101, "Jiphin", "Savings", 1000)
b.deposit(500)
b.withdraw(300)
b.withdraw(1500)

# OUTPUT:
# Amount Deposited. New Balance: 1500
# Amount Withdrawn. New Balance: 1200
# Insufficient Balance