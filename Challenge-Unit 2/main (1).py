class BankAccount:
    def __init__(self, account_number, account_holder_name, initial_balance=0.0):
        self.__account_number = account_number
        self.__account_holder_name = account_holder_name
        self.__account_balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__account_balance += amount
            return f"₹{amount} deposited successfully."
        else:
            return "Invalid deposit amount."

    def withdraw(self, amount):
        if 0 < amount <= self.__account_balance:
            self.__account_balance -= amount
            return f"₹{amount} withdrawn successfully."
        else:
            return "Insufficient funds or invalid withdrawal amount."

    def display_balance(self):
        return f"Account Balance for {self.__account_holder_name}: ₹{self.__account_balance}"

# Creating an instance of BankAccount
account1 = BankAccount("00001", "John Doe", 1000.0)

# Testing deposit and withdrawal functionality
print(account1.display_balance())
print(account1.deposit(500))
print(account1.display_balance())
print(account1.withdraw(200))
print(account1.display_balance())
print(account1.withdraw(1500))  # This should result in an error message

