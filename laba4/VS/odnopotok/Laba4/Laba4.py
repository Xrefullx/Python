import  time
class Student(object):
    def __init__(self, number, korpus, propusk, size):
        self.number = number
        self.korpus = korpus
        self.propusk = propusk
        self.size = size

class Proverka():

    def stop(self, students, x, y):
        for i in students:
            if (i.size > x * y):
                print('Номер студента:', i.number,'Корпус:', i.korpus)

    def propusk_check(self, students):
        for i in students:
            if (i.propusk == False):
                print('Номер студента:', i.number,'Корпус:', i.korpus)

    def max_bag(self, students):
        max = 0
        for i in students:
            if (i.size > max):
                max = i.size
        for i in students:
            if (i.size == max):
                print('Номер студента:', i.number,'Корпус:', i.korpus, 'Размер', i.size)


students = []
students.append(Student(1, "ИКИТ", True, 35))
students.append(Student(3, "ПИ", False, 15))
students.append(Student(1, "ИУБП", True, 11))
students.append(Student(3, "ПИ", False, 45))
students.append(Student(1, "ИКИТ", True, 55))
students.append(Student(3, "ПИ", False, 42))
students.append(Student(1, "ИКИТ", True, 233))
students.append(Student(3, "ПИ", False, 5))
students.append(Student(1, "ИКИТ", True, 64))
students.append(Student(3, "ПИ", False, 23))
students.append(Student(1, "ИКИТ", True, 25))
students.append(Student(3, "ПИ", False, 25))
students.append(Student(1, "ИКИТ", True, 35))
students.append(Student(3, "ПИ", False, 15))
students.append(Student(1, "ИУБП", True, 11))
students.append(Student(3, "ПИ", False, 45))
students.append(Student(1, "ИКИТ", True, 55))
students.append(Student(3, "ПИ", False, 42))
students.append(Student(1, "ИКИТ", True, 233))
students.append(Student(3, "ПИ", False, 5))
students.append(Student(1, "ИКИТ", True, 64))
students.append(Student(3, "ПИ", False, 23))
students.append(Student(1, "ИКИТ", True, 25))
students.append(Student(3, "ПИ", False, 25))
students.append(Student(1, "ИКИТ", True, 35))
students.append(Student(3, "ПИ", False, 15))
students.append(Student(1, "ИУБП", True, 11))
students.append(Student(3, "ПИ", False, 45))
students.append(Student(1, "ИКИТ", True, 55))
students.append(Student(3, "ПИ", False, 42))
students.append(Student(1, "ИКИТ", True, 233))
students.append(Student(3, "ПИ", False, 5))
students.append(Student(1, "ИКИТ", True, 64))
students.append(Student(3, "ПИ", False, 23))
students.append(Student(1, "ИКИТ", True, 25))
students.append(Student(3, "ПИ", False, 25))
students.append(Student(1, "ИКИТ", True, 35))
students.append(Student(3, "ПИ", False, 15))
students.append(Student(1, "ИУБП", True, 11))
students.append(Student(3, "ПИ", False, 45))
students.append(Student(1, "ИКИТ", True, 55))
students.append(Student(3, "ПИ", False, 42))
students.append(Student(1, "ИКИТ", True, 233))
students.append(Student(3, "ПИ", False, 5))
students.append(Student(1, "ИКИТ", True, 64))
students.append(Student(3, "ПИ", False, 23))
students.append(Student(1, "ИКИТ", True, 25))
students.append(Student(3, "ПИ", False, 25))
students.append(Student(1, "ИКИТ", True, 35))
students.append(Student(3, "ПИ", False, 15))
students.append(Student(1, "ИУБП", True, 11))
students.append(Student(3, "ПИ", False, 45))
students.append(Student(1, "ИКИТ", True, 55))
students.append(Student(3, "ПИ", False, 42))
students.append(Student(1, "ИКИТ", True, 233))
students.append(Student(3, "ПИ", False, 5))
students.append(Student(1, "ИКИТ", True, 64))
students.append(Student(3, "ПИ", False, 23))
students.append(Student(1, "ИКИТ", True, 25))
students.append(Student(3, "ПИ", False, 25))
students.append(Student(1, "ИКИТ", True, 35))
students.append(Student(3, "ПИ", False, 15))
students.append(Student(1, "ИУБП", True, 11))
students.append(Student(3, "ПИ", False, 45))
students.append(Student(1, "ИКИТ", True, 55))
students.append(Student(3, "ПИ", False, 42))
students.append(Student(1, "ИКИТ", True, 233))
students.append(Student(3, "ПИ", False, 5))
students.append(Student(1, "ИКИТ", True, 64))
students.append(Student(3, "ПИ", False, 23))
students.append(Student(1, "ИКИТ", True, 25))
students.append(Student(3, "ПИ", False, 25))
math.factorial(10000)
startTime = time.time()
cam1 = Proverka()
print("Студенты которых нужно остановить:")
cam1.stop(students, 10, 5)
print("Студенты у которых нет пропуска:")
cam1.propusk_check(students)
print("Студент с самой большой сумкой:")
cam1.max_bag(students)


endTime = time.time()
print ("Время выполнения: ", endTime - startTime)
i=0
for item in students:
      i=i+1
print(i)