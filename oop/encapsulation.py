class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance #private variable
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"${amount} deposited. New balance: ${self.__balance}")
    
    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"${amount} withdrawn. Remaining balance: ${self.__balance}")
        else:
            print("Insufficient funds!")
            
            
account = BankAccount("Abenezer", 1000)
account.withdraw(500)