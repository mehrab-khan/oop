#how to make a template by class and inner instance


# class Employee:
#     def __init__(self, fname, lname, slary): #constructor
#         self.fname = fname
#         self.lname = lname
#         self.salary = slary
#
#
#
# harry = Employee("Mehrab","Khan",4500)
# elif_bilge = Employee("Elif","Parlak", 4500)
#
#
# print(harry.fname, elif_bilge.lname)


#

class Employee:
    increament = 2
    number_of_employee = 0
    def __init__(self, fname, lname, salary): #constructor
        self.fname = fname
        self.lname = lname
        self.salary = salary
        self.increament = 5
        Employee.number_of_employee += 1
    def Increament(self):
        self.salary = int(self.salary * self.increament)   #ei khan e self.increament dile eta dekhbe instance e increament ache kina
        #na thakle tokhon class er ta access nibe increament

        #Employee.increament dile class er moddher increament ke access nibe





# print(harry.salary) #before use increament function salary
# harry.Increament()
# print(harry.salary)#after use increament function salary
#
#
#
# print(harry.__dict__)  # instance er moddher sob variable dekhar jonno
# harry.address = "Dhaka" # new add a variable in instance
# print(harry.__dict__)   #after add a new variable lets check it
# print(Employee.__dict__)  #check class variables
#
print(Employee.number_of_employee)
harry = Employee("Mehrab","Khan",4500)
print(Employee.number_of_employee)
elif_bilge = Employee("Elif","Parlak", 4000)
print(Employee.number_of_employee)