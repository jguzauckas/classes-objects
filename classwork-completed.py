# Create a BankAccount class that has a variable for name (str)
# and balance (float).
#
# Make sure you have __init__() and __str__() functions, and
# have the __str__() function format the balance to two decimal places.
#
# balance should be a property with a getter
# and setter method. Have the setter method check to make sure
# balance is not being set to a negative number.
#
# Create a method called payday that when called will add a predetermined
# amount to the account and return the new balance value.
#
# Create another method called spend that when called will subtract
# a parameter amount from the balance ONLY IF it is not bigger than
# the balance. If it is bigger than the balance, print a statement
# letting the user know about the issue. Don't return anything.
class BankAccount:
    def __init__(self, name: str, val: float) -> None:
        self.name = name
        self._balance = val

    def __str__(self) -> str:
        return f"{self.name} has ${self._balance:.2f} in their account."

    @property
    def balance(self) -> float:
        return self._balance

    @balance.setter
    def balance(self, val: float) -> None:
        if val >= 0:
            self._balance = val
        else:
            print("Bank accounts can't have negative money!")

    def payday(self) -> float:
        self._balance += 1000
        return self._balance

    def spend(self, amt: float) -> None:
        if amt < self._balance:
            self._balance -= amt
        else:
            print("You can't spend that much!")


# Test your class by creating two bank account objects with different
# names and balances.
b1 = BankAccount("Mr. Cawley", 11.11)
b2 = BankAccount("Mr. G", 11.12)

# Call the payday method on the first bank account and print out the
# current status of both accounts.
b1.payday()
print(b1)
print(b2)

# Try to spend more money than the second bank account has, making
# sure it stops you.
b2.spend(20.00)

# Spend a reasonable amount of money on both accounts and print
# out the current status of both accounts.
b1.spend(150.00)
b2.spend(10.00)
print(b1)
print(b2)
