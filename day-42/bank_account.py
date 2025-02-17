"""
Create a class for a bank account with methods for deposit and withdrawal.
"""

class BankAccount:

    def __init__(self, acc_no, balance):
        self.acc_no = acc_no
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print(f"Can't deposit R{amount}.")
        else:
            self.balance = self.balance + amount

    def withdraw(self, amount):
        if amount <= 0:
            print(f"Can't withdraw R{amount}.")
        elif amount > self.balance:
            print(f"Can't withdraw R{amount}, balance exceeded.")
        else:
            self.balance = self.balance - amount

    def get_current_balance(self):
        return self.balance


if __name__ == "__main__":
    acc = BankAccount("1001", 500)
    print("R", acc.get_current_balance())
    acc.deposit(300)
    print("R",acc.get_current_balance())
    acc.withdraw(700)
    print("R",acc.get_current_balance())

