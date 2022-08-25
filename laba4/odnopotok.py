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
students.append(Student(2, "ПИ", False, 15))
students.append(Student(3, "ИУБП", True, 11))
students.append(Student(4, "ПИ", False, 45))
students.append(Student(5, "ИКИТ", True, 55))
students.append(Student(6, "ПИ", False, 42))
students.append(Student(7, "ИКИТ", True, 233))
students.append(Student(8, "ПИ", False, 5))
students.append(Student(9, "ИКИТ", True, 64))
students.append(Student(10, "ПИ", False, 23))
students.append(Student(11, "ИКИТ", True, 25))
students.append(Student(12, "ПИ", False, 25))
students.append(Student(13, "ИКИТ", True, 35))
students.append(Student(14, "ПИ", False, 15))
students.append(Student(15, "ИУБП", True, 11))
students.append(Student(16, "ПИ", False, 45))
students.append(Student(17, "ИКИТ", True, 55))
students.append(Student(18, "ПИ", False, 42))
students.append(Student(19, "ИКИТ", True, 233))
students.append(Student(20, "ПИ", False, 5))
students.append(Student(21, "ИКИТ", True, 64))
students.append(Student(22, "ПИ", False, 23))
students.append(Student(23, "ИКИТ", True, 25))
students.append(Student(24, "ПИ", False, 25))
students.append(Student(25, "ИКИТ", True, 35))
students.append(Student(26, "ПИ", False, 15))
students.append(Student(27, "ИУБП", True, 11))
students.append(Student(28, "ПИ", False, 45))
students.append(Student(29, "ИКИТ", True, 55))
students.append(Student(30, "ПИ", False, 42))
students.append(Student(31, "ИКИТ", True, 233))
students.append(Student(32, "ПИ", False, 5))
students.append(Student(33, "ИКИТ", True, 64))
students.append(Student(34, "ПИ", False, 23))
students.append(Student(35, "ИКИТ", True, 25))
students.append(Student(36, "ПИ", False, 25))
students.append(Student(37, "ИКИТ", True, 35))
students.append(Student(38, "ПИ", False, 15))
students.append(Student(39, "ИУБП", True, 11))
students.append(Student(40, "ПИ", False, 45))
students.append(Student(41, "ИКИТ", True, 55))
students.append(Student(42, "ПИ", False, 42))
students.append(Student(43, "ИКИТ", True, 233))
students.append(Student(44, "ПИ", False, 5))
students.append(Student(45, "ИКИТ", True, 64))
students.append(Student(46, "ПИ", False, 23))
students.append(Student(47, "ИКИТ", True, 25))
students.append(Student(48, "ПИ", False, 25))
students.append(Student(49, "ИКИТ", True, 35))
students.append(Student(50, "ПИ", False, 15))
students.append(Student(51, "ИУБП", True, 11))
students.append(Student(52, "ПИ", False, 45))
students.append(Student(53, "ИКИТ", True, 55))
students.append(Student(54, "ПИ", False, 42))
students.append(Student(55, "ИКИТ", True, 233))
students.append(Student(56, "ПИ", False, 5))
students.append(Student(57, "ИКИТ", True, 64))
students.append(Student(58, "ПИ", False, 23))
students.append(Student(59, "ИКИТ", True, 25))
students.append(Student(60, "ПИ", False, 25))
students.append(Student(61, "ИКИТ", True, 35))
students.append(Student(62, "ПИ", False, 15))
students.append(Student(63, "ИУБП", True, 11))
students.append(Student(64, "ПИ", False, 45))
students.append(Student(65, "ИКИТ", True, 55))
students.append(Student(66, "ПИ", False, 42))
students.append(Student(67, "ИКИТ", True, 233))
students.append(Student(68, "ПИ", False, 5))
students.append(Student(69, "ИКИТ", True, 64))
students.append(Student(70, "ПИ", False, 23))
students.append(Student(71, "ИКИТ", True, 25))
students.append(Student(72, "ПИ", False, 25))
startTime = time.time()
lab4= Proverka()
print("Студенты которых нужно остановить:")
lab4.stop(students, 10, 5)
print("Студенты у которых нет пропуска:")
lab4.propusk_check(students)
print("Студент с самой большой сумкой:")
lab4.max_bag(students)


endTime = time.time()
print ("Время выполнения: ", endTime - startTime)
i=0
for item in students:
      i=i+1
print(i)