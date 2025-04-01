### Method OverLoading ###

print("\n $$$Method Overloading$$$ \n")

class Overloading_class:

    def overLoadingwithDefult(self, a=0, b=0, c=0, d=0): #for Default Value
        print(a+b)
        print(a+c)
        print(a+d)



    def overLoadingM(self,*a): #for Variable Lenth
        print(a)




overLoadingOBJ = Overloading_class()

overLoadingOBJ.overLoadingM(10,20,20,10,30,22,115,1154,1454,4646,4646,411,2121,124,46,455)
overLoadingOBJ.overLoadingwithDefult(1)
overLoadingOBJ.overLoadingwithDefult(2,20,30,40)