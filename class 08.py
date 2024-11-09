
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
        

    @property
    def email(self):
        if self.fname == None :
            return 'email not set'
        else:
            return self.fname + self.lname + '@gmail.com'
        

    @email.setter
    def email(self, given_email):
        name_list = given_email.split('@')[0].split('.')
        self.fname = name_list[0]
        self.lname = name_list[1]

    @email.deleter
    def email(self):
        self.fname = None
        self.lname = None






mehrab = Employee("Mehrab","khan",52000)
rashed = Employee("Rashed","khan",52000)

print(mehrab.email , rashed.email)
rashed.lname = "Howlader"
print(rashed.email)
rashed.email = 'howlader.rashed@gmail.com' #given email
print(rashed.email)


del rashed.email  

print(rashed.email)