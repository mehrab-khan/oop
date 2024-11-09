#class Methood
#ei khan e class ke as a argument niye classmethod er maddhom e, ekti value change kore jemon aage chilo
#increament 2 ekhn hoyeche 4 nicher dike
class Employee:
    increament = 2

    def __init__(self, fname, lname, salary): #constructor
        self.fname = fname
        self.lname = lname
        self.salary = salary


    def increase(self):
        self.salary = int(self.salary * self.increament)
    @classmethod
    def change_increament(cls, amount):
        cls.increament = amount

mehrab = Employee("Mehrab","Khan",120)
elif__ = Employee("Elif","Bilge",150)

print(mehrab.salary)
Employee.change_increament(5)
mehrab.increase()  #changed
print(mehrab.salary)