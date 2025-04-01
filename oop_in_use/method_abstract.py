### Abstract Method
from abc import ABC,abstractmethod

print("\n $$$Method Abscraction$$$ \n")

class Bangladesh(ABC):

    @abstractmethod
    def print1to5(self):
       pass

    @abstractmethod
    def print0to10(self):
        pass


class Dhaka(Bangladesh):
    def print1to5(self):
        for i in range(6):
            print(i)


    def print0to10(self):
        for i in range(11):
            print(i)


dh = Dhaka()

dh.print1to5()