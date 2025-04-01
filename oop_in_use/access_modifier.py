### Access Modifier ###
print("\n $$$Access Modifier$$$ \n")
class Banks:
    bank_name = "Pyhon Bank LTD." #public
    branch = "Cyber World"  #public
    _total_user = 215   #protected
    __my_total_balance = 250000 #privet




class MyBank(Banks):
    def bank_details(self):
        print(self.bank_name)   #Output: Pyhon Bank LTD.
        print(self.branch)  #Output: Cyber World
        print(self._total_user) #Output: 215
       # print(self.__my_total_balance) # Output: Nothing...



myBankObj = MyBank()
myBankObj.bank_details()