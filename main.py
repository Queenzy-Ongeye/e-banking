from datetime import datetime
from hmac import trans_36


class Account:
    typeAcc = "Saving Account"

    def __init__(self, name, accNumber):
        self.name = name
        self.accNumber = accNumber
        self.balance = 0
        self.depositos = []
        self.deposits = []
        self.withdrawals = []
        self.withs = []
        self.transactions = 100
        self.date = datetime.now()
        self.state = self.date.strftime("%d/%m/%y")
        # Add a new attribute loan_balance which is zero by default.
        self.loan_balance = 0
        self.accBalance = 0
        self.transaction = 0

    def deposit(self, money):
        self.money = money
        if money <= 0:
            return f"You have insufficient funds to deposit"
        else:
            self.balance += money
            self.depositos.append(money)
            print(self.depositos)

            # Update the deposit method to store each deposit transaction as a dictionary like this
            self.deposits.append(
                {'date': self.state, 'amount': money, 'narration': 'Deposit'})
            print(
                f"You have deposited {money} and your balance is {self.balance}")
            return f"{self.deposits}"

    def withdraw(self, amount):
        money = amount + self.transactions
        if money >= self.balance:
            return f"You cannot withdraw this amount"
        elif amount <= 0:
            return f"You cannot withdraw {amount} and you balance is {self.balance}."
        else:
            self.balance -= money
            self.withs.append(amount)
            print(f"{self.withs}")
            # Update the withdraw method to store each deposit transaction as a dictionary like this

            self.withdrawals.append(
                {'date': self.state, 'amount': amount, 'narration': 'Withdrawal'})
            print(
                f"You have withdrawn {amount} and your balance is {self.balance}")
            return f"{self.withdrawals}"

    def depo_status(self):
        for money in self.depositos:
            print(money)

    def with_stats(self):
        for money in self.withs:
            print(money)

    def show_balance(self):
        return f"{self.balance}"


# Add a new method  full_statement which combines both
# deposits and withdrawals into one list ordered by date
# and using a for loop prints each transaction in a new line like this


    def full_statement(self):
        states = self.deposits + self.withdrawals
        for state in states:
            print(state)

# Add a borrow method which allows a customer to borrow if they meet these conditions:
# Customer has made at least 10 deposits.
# Loan amount requested must be more than 100
# A customer qualifies for a loan amount that is less than  or equal to 1/3 of their total sum of deposit history
# Customer account has no has no balance
# Customer has no outstanding loan
# The loan attracts  an interest of 3%.
    def borrow(self, amount):
        self.amount = amount
        self.loan_balance += self.amount
        sum = 0
        for money in self.deposits:
            sum += money["amount"]
        if len(self.depositos) <= 10:
            self.loan_balance = 0
            return f"Your deposits must be more than 10 to get a loan"
        elif self.amount < 100:
            self.loan_balance = 0
            return f"You cannot borrow below 100"
        elif self.amount < (sum//3):
            return f"You loan balance is {self.loan_balance}"
        elif self.balance == 0:
            return f"You cannot borrow"
        elif self.loan_balance > 0:
            return f"Your loan of {self.loan_balance} is still pending, please pay in order to get a new loan"
        else:
            self.loan_balance = (0.03*self.amount) + self.amount
            return f"Your loan balance is {self.loan_balance}"

 # Add a loan repayment method with these conditions
        # A customer can repay a loan to reduce the current loan balance
        # Overpayment of a loan increases a customers current deposit

    def loan_repay(self, cash):
        if cash == self.amount:
            self.loan_balance = cash - self.amount
            print(f"Your current loan of {self.amount} balance is fully paid")
        elif cash > self.loan_balance:
            self.loan_balance -= self.loan_balance
            remaining_balance = cash - self.amount
            new_depo_balance = self.balance + remaining_balance
            return f"Your loan of {self.amount} if fully paid. Your remaining balance of {remaining_balance} has been added to your deposit account.Your new deposit balance is{new_depo_balance}. Your loan balance is {self.loan_balance}"
    
    # Add a new method transfer which accepts two attributes 
    # (amount and instance of another account). If the amount 
    # is less than the current instances balance, the method 
    # transfers the requested amount from the current account 
    # to the passed account. The transfer is accomplished by 
    # reducing the current account balance and depositing the 
    # requested amount to the passed account.

    def transfer(self, amount, account):
        self.account = account
        if amount < self.balance:
            moneyTransfer = self.balance - self.transaction
            self.transaction = self.balance - amount
            self.accBalance += amount
            return f"Money transfer of {amount} from {self.name} has been sent to {self.account}. Your new balance will be {moneyTransfer}. {self.account} new balance is {self.accBalance}"


