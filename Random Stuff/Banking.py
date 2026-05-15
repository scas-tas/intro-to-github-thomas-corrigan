class Account:
    def __init__(self, number, balance, owner):
       self.number = number
       self.balance = balance
       self.owner = owner

    def deposit(self, amount):
       self.balance += amount 

    def withdraw(self, amount):
       self.balance -= amount

    def __str__(self):
       return f"Name: {self.owner}, Balance: {self.balance}"

    def print_attrib(self):
       print(f"Name: {self.owner}, Balance: {self.balance}")

       
# Mainline
alice = Account("12345", 1000, "Alice")
hugo = Account("57167", 51002, "Hugo")
thomas = Account("743321", 97155678, "Thomas")




