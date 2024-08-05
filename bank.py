# Create a Python class called BankAccount which represents a bank account, having as attributes: accountNumber (numeric type), name (name of the account owner as string type), balance.
# Create a constructor with parameters: accountNumber, name, balance.
# Create a Deposit() method which manages the deposit actions.
# Create a Withdrawal() method which manages withdrawals actions.
# Create an bankFees() method to apply the bank fees with a percentage of 5% of the balance account.
# Create a display() method to display account details. Give the complete code for the BankAccount class.
# Eg. After making above classes and methods, on executing below code:-

# newAccount = BankAccount(2178514584, "Mandy" , 2800)

# newAccount.Withdrawal(700)

# newAccount.Deposit(1000)

# newAccount.display()
# Output:

# Account Number :  2178514584
# Account Name :  Mandy
# Account Balance :  3100 ₹

class BankAccount:
    def __init__(self, accountnumber, name, balance):
        self.accountnumber = accountnumber
        self.name = name
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited: {amount} ")

    def withdrawal(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount
            print(f"Withdrawn: {amount} ")

    def bank_fees(self):
       self.balance *= 0.95

    def display(self):
        print(f"Account Number: {self.accountnumber}")
        print(f"Account Name: {self.name}")
        print(f"New balance after deducting 5% : {self.balance} Rs")


newAccount = BankAccount(2178514584, "Mandy" , 1000)



newAccount.withdrawal(700)
newAccount.deposit(1000)
newAccount.bank_fees()
newAccount.display()
