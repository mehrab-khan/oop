class Employee:
    bonus = 2000
    def __init__(self,name,id,shift,salary):
        self.name = name
        self.id = id
        self.shift = shift
        self.salary = salary
    def increase_salary(self):
        self.salary = self.salary + self.bonus

    @classmethod
    def change_bonus(cls, given_bonus):
        cls.bonus = given_bonus
    @staticmethod
    def printf():
        print("Paid Done")
    def __add__(self,other):
        return self.salary + other.salary
    @property
    def email(self):
        if self.name == None:
            return 'Sorry Pookie'
        else:
            return self.name + '@gmail.com'

    @email.setter
    def email(self,givenMail):
        newEmail = givenMail.split('@')[0]
        self.name = newEmail

    @email.deleter
    def email(self):
        self.name = None


rashed = Employee("Rashed",24,'Day',24000)
print(rashed.email)
print(rashed.name)
rashed.email = 'zakar@gmail.com'
print(rashed.email)

print(rashed.name)

print(rashed.salary)
rashed.change_bonus(5000)
rashed.increase_salary()
print(rashed.salary)
print(rashed.email)
del rashed.email
print(rashed.email)

nadia = Employee("Nadia",12,"Day",45000)
print(rashed + nadia)