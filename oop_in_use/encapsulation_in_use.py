### Encapsulation ###
print("\n $$$Encapsulation$$$ \n")
class BankAccount:
    __Balance = 0

    #deposit
    def deposit(self,amount):
        if amount >= 0:
            self.__Balance += amount
            print(f"Your Amount ${amount} is successfully Deposited!\nYour current balance is ${self.__Balance}, Thank you.")

        else: print("Invalid Amount! Please Try with a valid Amount.")

    
    #Withdraw
    def withdraw(self,amount):
        if amount > 0 and amount <= self.__Balance:
            self.__Balance -= amount
            print(f"Your withdraw request amount ${amount} has been successfully procced.\nYour current balance is ${self.__Balance}, Thank you.")

        else: print("Sorry, You Dont have sufficient balance. try leter.")
        


    #Balance Check
    def balance_check(self):
        return f"Your current balance is ${self.__Balance}, Thank you."



bankAccount = BankAccount()
bankAccount.deposit(2000)
bankAccount.withdraw(1500)
print(bankAccount.balance_check())