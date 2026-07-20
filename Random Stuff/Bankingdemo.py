# =============================================================================
# BANK ACCOUNT SYSTEM
# St Columba Anglican School — Year 11 Software Engineering
# =============================================================================
#
# This file demonstrates key Object-Oriented Programming (OOP) concepts:
#
#   - Classes and Objects       A class is a blueprint; an object is a
#                               specific thing made from that blueprint.
#
#   - Encapsulation             Each class bundles its own data (attributes)
#                               and behaviour (methods) together.
#
#   - Abstraction               When you call account.deposit(100), you don't
#                               need to know HOW it works internally — just
#                               what it does.
#
#   - Inheritance               SavingsAccount and CheckingAccount both
#                               inherit from Account, meaning they get all of
#                               Account's methods for free.
#
#   - Polymorphism              Both child classes have a withdraw() method,
#                               but each one behaves differently.
#
#   - Message Passing           The Customer class asks each Account object
#                               to report its balance — objects communicating
#                               with each other.
#
# =============================================================================


# =============================================================================
# CLASS: Account  (the PARENT class)
# =============================================================================

class Account:
    """
    A basic bank account.

    This is the PARENT (or BASE) class. SavingsAccount and CheckingAccount
    will both inherit from this class.

    Attributes:
        number  (str)   : the account number, e.g. "12345"
        balance (float) : the current balance in dollars
        owner   (str)   : the name of the account holder
    """

    def __init__(self, number, balance, owner):
        """
        Constructor — runs automatically when you create a new Account object.

        The 'self' parameter refers to the specific object being created.
        Think of it as the object introducing itself: "I am THIS account."
        """
        self.number = number      # Store the account number on this object
        self.balance = balance    # Store the starting balance on this object
        self.owner = owner        # Store the owner's name on this object

    def deposit(self, amount):
        """
        Add money to the account.

        Validates the amount before depositing — negative deposits and
        zero deposits are rejected.
        """
        # Check for invalid amounts first
        if amount <= 0:
            print("Deposit amount must be greater than zero.")
            return   # Stop here — don't add anything

        # Amount is valid, so add it to the balance
        self.balance += amount
        print(f"Deposited ${amount:.2f}. New balance: ${self.balance:.2f}")

    def withdraw(self, amount):
        """
        Remove money from the account.

        Validates the amount and checks there are sufficient funds.
        Child classes (SavingsAccount, CheckingAccount) OVERRIDE this
        method to add their own extra rules.
        """
        # Reject invalid amounts
        if amount <= 0:
            print("Withdrawal amount must be greater than zero.")
            return

        # Reject if there isn't enough money
        if amount > self.balance:
            print(f"Insufficient funds. Balance is ${self.balance:.2f}.")
            return

        # All checks passed — process the withdrawal
        self.balance -= amount
        print(f"Withdrew ${amount:.2f}. New balance: ${self.balance:.2f}")

    def add_interest(self, rate):
        """
        Apply interest to the account balance.

        Args:
            rate (float): the interest rate as a decimal, e.g. 0.05 for 5%
        """
        interest = self.balance * rate          # Calculate interest earned
        self.balance += interest                # Add it to the balance
        print(f"Interest added: ${interest:.2f}. New balance: ${self.balance:.2f}")

    def check_balance(self):
        """
        Display the current account balance.
        """
        print(f"Account {self.number} ({self.owner}): ${self.balance:.2f}")


# =============================================================================
# CLASS: SavingsAccount  (a CHILD class of Account)
# =============================================================================

class SavingsAccount(Account):
    """
    A savings account with a minimum balance requirement.

    INHERITS from Account — meaning it automatically gets deposit(),
    check_balance(), and add_interest() without us rewriting them.

    The only method we need to change is withdraw(), because savings accounts
    have an extra rule: the balance can't drop below the minimum.

    New Attribute:
        min_balance (float): the minimum balance that must remain at all times
    """

    def __init__(self, number, balance, owner, min_balance):
        """
        Constructor for SavingsAccount.

        We call super().__init__() to run Account's constructor first —
        this sets up number, balance, and owner. Then we add min_balance.
        """
        super().__init__(number, balance, owner)   # Set up inherited attributes
        self.min_balance = min_balance              # Add the new attribute

    def withdraw(self, amount):
        """
        Withdraw from a savings account — respecting the minimum balance.

        This OVERRIDES Account's withdraw() method. It adds one extra check
        before deciding whether to proceed.

        This is POLYMORPHISM: same method name (withdraw), different behaviour.
        """
        # First, check the standard validation (positive amount, etc.)
        if amount <= 0:
            print("Withdrawal amount must be greater than zero.")
            return

        # Extra savings rule: would this take us below the minimum balance?
        if self.balance - amount < self.min_balance:
            print(
                f"Cannot withdraw ${amount:.2f}. "
                f"That would go below the minimum balance of ${self.min_balance:.2f}. "
                f"Current balance: ${self.balance:.2f}"
            )
            return

        # All checks passed — process the withdrawal
        self.balance -= amount
        print(f"Withdrew ${amount:.2f}. New balance: ${self.balance:.2f}")


# =============================================================================
# CLASS: CheckingAccount  (another CHILD class of Account)
# =============================================================================

class CheckingAccount(Account):
    """
    A checking (everyday) account that allows overdrafts up to a set limit.

    INHERITS from Account — same idea as SavingsAccount.

    Again, only withdraw() needs to change. The overdraft rule replaces the
    "can't go negative" rule from the parent class.

    New Attribute:
        overdraft_limit (float): how far into the negative the balance can go
    """

    def __init__(self, number, balance, owner, overdraft_limit):
        """
        Constructor for CheckingAccount.
        """
        super().__init__(number, balance, owner)    # Set up inherited attributes
        self.overdraft_limit = overdraft_limit      # Add the new attribute

    def withdraw(self, amount):
        """
        Withdraw from a checking account — allowing overdraft up to the limit.

        This OVERRIDES Account's withdraw() differently from SavingsAccount.
        Same method name, completely different rule — this is POLYMORPHISM.
        """
        # Check for invalid amounts
        if amount <= 0:
            print("Withdrawal amount must be greater than zero.")
            return

        # Would this withdrawal exceed the overdraft limit?
        # e.g. balance = $50, overdraft_limit = $500
        # Withdrawal of $600 would give us -$550, which is past -$500
        if self.balance - amount < -self.overdraft_limit:
            print(
                f"Cannot withdraw ${amount:.2f}. "
                f"Overdraft limit is ${self.overdraft_limit:.2f}."
            )
            return

        # All checks passed — process the withdrawal (may result in negative balance)
        self.balance -= amount
        print(f"Withdrew ${amount:.2f}. New balance: ${self.balance:.2f}")


# =============================================================================
# CLASS: Customer  (uses COMPOSITION — a Customer HAS accounts)
# =============================================================================

class Customer:
    """
    A bank customer who can hold multiple accounts.

    This class demonstrates TWO important ideas:

    COMPOSITION: A Customer object CONTAINS Account objects.
                 This is different from inheritance — Customer doesn't extend
                 Account, it simply HAS a list of them.
                 "Has-a" relationship vs "Is-a" relationship.

    MESSAGE PASSING: When we call total_balance(), the Customer object sends
                     a message to each Account object, asking for its balance.
                     Objects talking to other objects = message passing.

    Attributes:
        name     (str)  : the customer's full name
        accounts (list) : a list of Account objects belonging to this customer
    """

    def __init__(self, name):
        """
        Constructor for Customer.

        We start with an empty list of accounts. Accounts are added later
        using the add_account() method.
        """
        self.name = name
        self.accounts = []      # Start with no accounts — we'll add them below

    def add_account(self, account):
        """
        Add an account to this customer's list.

        Args:
            account: any Account object (Account, SavingsAccount, CheckingAccount)
        """
        self.accounts.append(account)
        print(f"Account {account.number} added for {self.name}.")

    def total_balance(self):
        """
        Calculate and display the total balance across all of this customer's accounts.

        This is MESSAGE PASSING in action:
        - The Customer object loops through its accounts
        - For each account, it accesses the balance attribute
        - Each Account responds with its own balance data
        """
        total = 0

        print(f"\n{self.name}'s Accounts:")
        print("-" * 35)

        # Loop through every account this customer owns
        for account in self.accounts:
            # Ask each account object for its current balance
            print(f"  Account {account.number}: ${account.balance:.2f}")
            total += account.balance    # Add it to the running total

        print("-" * 35)
        print(f"  Total: ${total:.2f}\n")

    def find_account(self, number):
        """
        Search for an account by its account number.

        Args:
            number (str): the account number to search for

        Returns:
            The matching Account object, or None if not found.
        """
        # Loop through accounts looking for a match
        for account in self.accounts:
            if account.number == number:
                return account     # Found it — return the account object

        # If we get here, no match was found
        return None


# =============================================================================
# DEMONSTRATION
# Running this section shows all the OOP concepts working together.
# =============================================================================

print("=" * 50)
print("BANK ACCOUNT SYSTEM — OOP DEMONSTRATION")
print("=" * 50)


# --- Create accounts (objects from classes) ---
print("\n--- Creating Accounts ---")

# A basic account (no special rules)
general = Account("ACC001", 1000, "Alice")

# A savings account — can't drop below $200
savings = SavingsAccount("SAV001", 800, "Alice", 200)

# A checking account — can overdraft up to $500
checking = CheckingAccount("CHK001", 300, "Bob", 500)


# --- Test Account (parent class) ---
print("\n--- Testing Account (basic rules) ---")
general.check_balance()
general.deposit(200)
general.withdraw(50)
general.withdraw(2000)    # Should fail — insufficient funds
general.withdraw(-10)     # Should fail — invalid amount
general.add_interest(0.05)
general.check_balance()


# --- Test SavingsAccount (minimum balance rule) ---
print("\n--- Testing SavingsAccount (minimum balance = $200) ---")
savings.check_balance()
savings.withdraw(500)     # Should fail — would drop below $200 minimum
savings.withdraw(50)      # Should succeed — leaves $250, above $200 minimum
savings.check_balance()


# --- Test CheckingAccount (overdraft allowed) ---
print("\n--- Testing CheckingAccount (overdraft up to $500) ---")
checking.check_balance()
checking.withdraw(700)    # Should succeed — $300 - $700 = -$400, within -$500 limit
checking.check_balance()  # Balance will be negative
checking.withdraw(200)    # Should fail — -$400 - $200 = -$600, exceeds -$500 limit


# --- Demonstrate Polymorphism ---
print("\n--- Demonstrating Polymorphism ---")
print("Both accounts use withdraw(), but behave differently:\n")

savings2 = SavingsAccount("SAV002", 500, "Carol", 100)
checking2 = CheckingAccount("CHK002", 500, "Dave", 300)

# Same method call, completely different rules being applied
savings2.withdraw(450)    # Savings: check minimum balance
checking2.withdraw(450)   # Checking: check overdraft limit


# --- Create a Customer and demonstrate message passing ---
print("\n--- Creating Customer and Demonstrating Message Passing ---")

# Create a customer
alice = Customer("Alice Johnson")

# Create fresh accounts for Alice
alice_savings = SavingsAccount("SAV010", 2000, "Alice Johnson", 500)
alice_checking = CheckingAccount("CHK010", 800, "Alice Johnson", 1000)

# Add accounts to the customer (composition — Alice HAS accounts)
alice.add_account(alice_savings)
alice.add_account(alice_checking)

# Customer asks each account for its balance (message passing)
alice.total_balance()

# Use find_account to retrieve a specific account
found = alice.find_account("SAV010")
if found:
    found.deposit(500)    # Deposit into the found account

# Check the total again — it should have changed
alice.total_balance()


print("=" * 50)
print("END OF DEMONSTRATION")
print("=" * 50)