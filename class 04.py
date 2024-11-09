#normal function in class

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
print(Employee.is_open('monday'))