# Create 3 files in the classes directory car.py, fruit.py, and bank.py. 
# Define the following classes in each module respectively. 
# Car
# Fruit
# Account
# Each class should have one class attribute and three instance variables.

class Account:
    def __init__(self,account_number,balance,fees,interests):
        self.account_number=account_number
        self.balance=balance
        self.fees=fees
        self.interests=interests
    def account_number(self):
        return f"Her account number was (self.account_number)"