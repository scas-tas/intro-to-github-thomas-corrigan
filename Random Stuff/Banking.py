import sys
import time
import tkinter as tk



window = tk.Tk()
window.title("Tom's Super Fantastic Banking System!!!!!!")
window.geometry("640x480") 



class Bank:
   def __init__(self, number, balance, owner):
      self.number = number
      self.balance = balance
      self.owner = owner

   def deposit(self, amount):
      self.balance += amount
      print(f"New Balance: {self.balance}")

   def withdraw(self, amount):
      if amount > self.balance:
         print("Insufficient funds")
      else:
         self.balance -= amount
         print(f"Withdrew: ${amount}")
         print(f"New Balance: {self.balance}")

   def __str__(self):
      return f"Balance: {self.balance}"

   def print_attrib(self):
      print(f"Name: {self.owner}, Balance: {self.balance}")

       


active_function = "none"



# alice = Bank("12345", 1000, "Alice")
# hugo = Bank("57167", 51002, "Hugo")
# thomas = Bank("241209", 97155678, "Thomas")

users = [
    {"name": "Thomas", "number": 12345, "balance": 952.65},
    {"name": "Hugo",   "number": 54321, "balance": 2345652},
    {"name": "Alice",  "number": 44444, "balance": 2345652},
]

# Build the accounts dict from the users list
accounts = {u["number"]: Bank(u["number"], u["balance"], u["name"]) for u in users}


# account1 = accounts[int(input("What is the account number: "))]

# (account1).print_attrib()


def start():
   active_function = "none"
   counter = 0
   print("Welcome to Tom's Super Fantastic Banking System!!!!!!")
   print("")
   # setaccount = int(input("What is the account number: "))

   # setaccount = accounts[int(input("What is the account number: "))]

   while True:
      setaccount = int(input("What is the account number: "))
      
      setaccount1 = int(setaccount)
      if setaccount1 not in accounts:

         print("No user exists with that number, Please enter again: ")
         counter += 1
         if counter > 5:
            print("Too many attempts. Account locked")
            time.sleep(5)
            sys.exit()
      else: 
         break
   account1 = accounts[setaccount]
   active_function = input("What action would you like to perform? (q)uit, (d)eposit, (w)ithdraw, view (b)alance: ")

   if active_function == "q":
      sys.exit()
   elif active_function == "d":
      howmuch = int(input("How Much: "))
      (account1).deposit(howmuch)
   elif active_function == "w":
      howmuch1 = int(input("How Much: "))
      (account1).withdraw(howmuch1)
   elif active_function == "b":
      print(account1)


button = tk.Button()




# while True:
start()
window.mainloop()