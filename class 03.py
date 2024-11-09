#class method ke alternative constructor hisebe use
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

    @classmethod #use like an constructor
    def from_str(cls, emp_string):
        fname, lname, salary = emp_string.split('-')
        return cls(fname, lname, salary)

mehrab = Employee("Mehrab","Khan",120)
elif__ = Employee("Elif","Bilge",150)
lovish = Employee.from_str('Lovish-Inya-450')

print(lovish.salary)