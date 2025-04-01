### OPP Method Overriding ###

print("\n $$$Method Overriding$$$ \n")

class Father:
    personalInfo = {
        "name" : "Bablu Sardar",
        "age": 52,
        "weight": 82,
        "height" : "5'6"
    }

    properties = {
        "land": True,
        "home": True,
        "car" : True,
        "bankBalance": 500000
    }

    def __init__(self) -> None:
        pass


class Son(Father):
    son_BankBalance = 150000

    def sonsProperties(self):
        print("Father's Properties is: ")
        for i in self.properties.keys():
            print(f"{i} : {self.properties[i]}")


    def son_TotalB(self):
        dad_intBalance = int(self.properties["bankBalance"])
        son_intBalance = int(self.son_BankBalance)
        return dad_intBalance + son_intBalance

son = Son()
son.sonsProperties()
print(f"Son's Current Balance is: {son.son_TotalB()} Taka Only")
