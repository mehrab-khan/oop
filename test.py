# class Student:
#     doubleFee = 2
#     def __init__(self,fname,lname,id,roll,fee):
#         self.fname = fname
#         self.lname = lname
#         self.id = id
#         self.roll = roll
#         self.fee = fee
#     def Double(self):
#         self.fee = int(self.fee * self.doubleFee)
#     @classmethod
#     def TripleFee(cls, amount):
#         cls.doubleFee = amount

#     @classmethod
#     def Add(cls, new):
#         name ,lname, id, roll, fee  = new.split('-')
#         return cls(name ,lname, id,roll,fee)
#     @staticmethod
#     def even_or_odd(n):
#         if n%2 == 0:
#             return True
#         else:
#             return False
 
#     @property
#     def email(self):
#         if self.fname == None:
#             return "There is no email"
#         else:
#             return self.fname + self.lname + '@gmail.com'
#     @email.setter
#     def email(self,given_email):
#         name_list = given_email.split('@')[0].split('.')
#         self.fname = name_list[0]
#         self.lname = name_list[1] 

#     @email.deleter
#     def email(self):
#         self.fname = None
#         self.lname = None




# nishat = Student("nishat","akter",52,258,2000)
# rana = Student("Rana",'khan',45,145,4000)
 

 
# print(nishat.email)
# nishat.lname = 'nafixa'
# print(nishat.email)
# nishat.email = 'nafixa.nishat@gmail.com'
# print(nishat.email)


# del nishat.email

# print(nishat.email)



# class Sir:
#     increment = 2
#     def __init__(self,fname, lname, fee):
#         self.fname = fname
#         self.lname = lname
#         self.fee = fee
#     def double(self):
#         self.fee = self.fee * self.increment
#     @classmethod
#     def modify(self, amount):
#         self.increment = amount
#
#     @staticmethod
#     def name():
#         print("I don't know the name")
#
#
#     def __add__(self,other):
#         return self.fee + other.fee
#
#     def __str__(self):
#         return f"my name is {self.fname + ' ' + self.lname} and my fee is {self.fee}"
#
#     def __repr__(self):
#         return f"In repr my name is {self.fname + ' ' + self.lname} and my fee is {self.fee}"
#
#     @property
#     def email(self):
#         if self.fname == None:
#             return "Sorry Pookie"
#         else:
#             return self.fname + self.lname + '@gmail.com'
#
#     @email.setter
#     def email(self , given_email):
#         name_list = given_email.split('@')[0].split('.')
#         self.fname = name_list[0]
#         self.lname = name_list[1]
#     @email.deleter
#     def email(self):
#         self.fname = None
#         self.lname = None
#
# class Madam(Sir):
#     def __init__(self,fname,lname,fee,roll):
#         super().__init__(fname,lname,fee)
#         self.roll = roll
#
#
# rayhan = Sir("Rayhan","Hasan",2000)
# print(rayhan.fee)
# rayhan.modify(4)
# rayhan.double()
# print(rayhan.fee)
#
# Sir.name()
#
#
#
# Nishat = Madam("Nishat","Rahman",4500,45)
# print(Nishat.roll)
# print(Nishat + rayhan)
#
# print(Nishat)
# print(repr(rayhan))
#
#
# #email
# print(rayhan.email)
#
# rayhan.email = 'sadia.rayhan@gmail.com'
# print(rayhan.email)
# print(rayhan.fname, rayhan.lname)
#
#
# del rayhan.email
# print(rayhan.email)
# print(rayhan.__dict__)


def calculation():
    user = input("Enter : ")
    res = eval(user)
    if res < 100:
        print("You need to study")
        print(res)
    else:
        print(res)

calculation()
