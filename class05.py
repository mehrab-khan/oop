
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

    @staticmethod
    def is_open(day):
        if day == 'monday':
            return True
        else:
            return False


class Programmer(Employee):
    def __init__(self, fname, lname, salary, language, exp):
        super().__init__(fname, lname, salary)
        self.language = language
        self.exp = exp
    def increase(self):
        self.salary = int(self.salary * self.increament + 7)


mehrab = Programmer("Mehrab","Hossain",2500000,"Python",4)
print(mehrab.language)