
from abc import ABC, abstractclassmethod
class Taxi (ABC):
    def __init__(self, nameDriver, number, cost):
       self.nameDriver = nameDriver
       self.number = number
       self.cost = cost
    @abstractclassmethod
    def Calculator(list):
        pass
#__str__(self) - вызывается функциями str, print и format. Возвращает строковое представление объекта.(текстом выводит короче)
# Нужно для вывода атрибутов класса, обращается к ним через self
    def __str__(self):
        return (f"Driver name: {self.nameDriver}, number of the car: {self.number}, the cost of travel: {self.cost}")


class Student(object):
    def __init__(self, name, age,  baggage):
         self.name = name
         self.age = age
         self.baggage = baggage

class Car (Taxi):
    @staticmethod
    def Calculator(list):
        VesBaggage = 0
        #Здесь i.baggage обращаается к атрибуту baggage  элементе списка
        for i in list:
            VesBaggage = VesBaggage + i.baggage
        if VesBaggage < 50 and len(list) <= 4:
            return True

class Truck (Taxi):
    @staticmethod
    def Calculator(list):
        if len(list) <= 2:
            return True

list = []
list.append(Student("aaa", 19, 3))
list.append(Student("bbb", 20, 7))
list.append(Student("ccc", 18, 5))

car1 = Car("mazda", 958, 200)
car2 = Truck("kamaz", 125, 500)


if car1.Calculator(list) == True:
    print(car1)

else:
    print(car2)

