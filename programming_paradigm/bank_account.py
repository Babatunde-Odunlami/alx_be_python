#Programming paradigm: OOP concepts- creating a class Bank Account 
class BankAccount:
    def __init__(self,initial_balance=0):
        self.account_balance=initial_balance  #initialize account balance to 0

    def deposit(self, amount):
        '''deposit function checking input for negative values'''
        if amount>=0: 
            self.account_balance += amount
        else:
            print(f"Deposit amount must be positive")

    def withdraw(self, amount):
        '''withdraw function check for negative entry and sufficient funds'''
        if amount >= 0:
            if amount <= self.account_balance:
                self.account_balance -= amount
               # print(f"withdraw: ${amount}")
                return True
            else:
                #print("Insufficient funds")
                return False
        else:
            print(f"Withdraw amount must be positive")

    def display_balance(self):
        '''account balance display function'''
        print(f"Current Balance: ${self.account_balance:.2f}")


