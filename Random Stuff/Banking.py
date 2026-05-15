class Account:
    def __init__(self, number, balance, owner):
       self.number = number
       self.balance = balance
       self.owner = owner

    def print_attrib(self):
       print(self.balance)
       print(self.owner)


       
# Mainline
alice = Account("12345", 1000, "Alice")
hugo = Account("57167", 51002, "Hugo")
thomas = Account("743321", 97155678, "Thomas")


for people in [hugo, thomas, alice]:
   print(people.owner)

hugo.print_attrib()
thomas.print_attrib()

