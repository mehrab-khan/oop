
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
        

    def __add__(self, other):
        return self.salary + other.salary
    
    

    def __repr__(self):
        return 'Employee({},{},{})'.format(self.fname, self.lname, self.salary)


    def __str__(self):
        return 'The name of employee is {}'.format(self.fname)









mehrab = Employee("Mehrab","khan",52000)
rashed = Employee("Rashed","khan",52000)


#Dunder methods you find more in doc
# x = 6
# print(x.__add__(8)) #sum numbers
# print(x.__mul__(8)) #multiply numbers

# print(mehrab + rashed) #i cant concatinate those it gives me an error
# now i use dunder method to concatinate those i use def __add__ to concatinate those salary

# print(mehrab + rashed)





#----------------


# print(mehrab) # <__main__.Employee object at 0x000001D9E9A15CD0> returns

#ami chai print(mehrab) dile er vitorer sob print hobe er jonno __repr__ use korte hobe

print(mehrab) # emon likhle str er moddhe ja ache tai asbe abr str na thakle
#tokhon __repr__ er ja ache tai asbe Employee details

#ar jodi kew str thaka sottew __repr__ jante cay tokhon
print(repr(mehrab)) #likhte hobe 



# repr and str are magic funtions