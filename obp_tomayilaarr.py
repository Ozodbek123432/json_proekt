#oop - obeytga yonaltirigan dasturlash (object origen progrming)
#vazifasi OC
#oop - 4 tugga oinladi
#1 meros olish
#2-ninkopsuinasa -
from tkinter.font import names

from objekt import Ozodbek
#4-obstrkshion- funksya  qaytaradigan funksiya
a = ["banab","olma","meva"]
a.remove("banab")
print(a)
class Transport :
    def __init__(self):
        self.bmw = "elektr"
        self.mers = "mator"
class ElectricCar(Transport):
     def __init__(self):
         super().__init__()
         self.dog_soft = self.bmw
     def super(self):
         return f"bmw elektr{self.dog_soft}"
class Motorcycl(Transport):
    def __init__(self):
        super().__init__()
        self.cat_soft = self.mers
    def super(self):
        return f"merst mator{self.cat_soft}"
print(ElectricCar().super(),Motorcycl().super())
class Shape:
    def __init__(self):
        self.circle =5+7
    def pro(self):
        return f"kvarrat oshrish ==  {5+8}"
class Circle:
    def __init__(self):
        self.circle = "SALOM"+"OK"
    def pro(self):
        return f"soz qoshish == {"SALOM"+"OK"}"
class Rectangl:
    def __init__(self):
        self.circle = 7 ** 2
    def pro(self):
        return f"kvarrat oshrish == {7 ** 2}"
print(f"salom {Shape().pro()}\n{Circle().pro()}\n{Rectangl().pro()}")
class Pleylist:
    def __init__(self):
        self.a = input("")
        self.b = ["salom"]
        self.c = ["kecha sensiz yotoma"]
        if self.a == "qoshiqlar":
            print(self.c)
        elif self.a == "salom":
            print(self.c)
        elif self.a == "hopiz":
            print(self.b)
    def pro(self):
        self.a = input("")
        self.b = ["salom"]
        self.c = ["kecha sensiz yotoma"]
        if self.a == "qoshiqlar":
            print(self.c)
        elif self.a == "salom":
            print(self.c)
        elif self.a == "hopiz":
            print(self.b)
obj = Pleylist()
print(Pleylist().pro())