### Getter & Setter ###
print("\n $$$Getter & Setter$$$ \n")
class Bank:
    bank_name = "Pyhon Bank LTD." #public
    branch = "Cyber World"  #public
    _total_user = 215   #protected
    __total_balance = 250000 #privete


    @property
    def TotalBalance(self):    #  __total_balance getter
        return self.__total_balance


    @TotalBalance.setter
    def TotalBalance(self,value):
        self.__total_balance = value

class MyBank(Bank):
    def bank_details(self):
        print(self.bank_name)   #Output: Pyhon Bank LTD.
        print(self.branch)  #Output: Cyber World
        print(self._total_user) #Output: 215
     #   print(self.__total_balance) # Output: Nothing...



bank = Bank()
print(bank.TotalBalance) #using Getter
print(bank.TotalBalance + 600000) #Using Setter
myBankObj = MyBank()
myBankObj.bank_details()