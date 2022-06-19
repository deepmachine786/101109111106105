# this is a main class of the class..
# string = "String is Immutable"
# print(string)
# print(string.swapcase())
# print(string.casefold())
# print(string.title())
# print(string.capitalize())


# ...............................Python class Object ............/
# class: Class is a blue print or prototype of any an object ..





from pkg_resources import empty_provider


class Dog:
    pass 


# Object : The Object is a entity of the state and behavior associalted with in .
objects = Dog() # this is a object of the class Dog ..

# creating a class with attribute ..

# class Dogs:

#     # ce=reate a attribute 
#     attr1 = " mammanl"

#     def __init__(self, name) -> None:
#         self.name = name 
    
#     attr1 = "google"

#     def speak(self) -> None: print("My name is {}".format(self.name))

    
    
# # accessing the attribue the 
# Rodger = Dogs("rodger")
# Tommy = Dogs("Tommy")
# print("Rodger is {}".format(Rodger.__class__.attr1))
# print("Tommy is also {}".format(Tommy.__class__.attr1))

# print(" My name is {}".format(Rodger.name))
# print("My name is {}".format(Tommy.name))

# Rodger.speak()
# Tommy.speak()


# Inheritance : Inheritance is a capacity of the change one class to aother clas. one class is 
# derived  n another class is called derived class and another class is child class ..

# class Person(object):

#     def __init__(self,name,idNumber) -> None:
#         self.name = name 
#         self.idNumber = idNumber

#     def display(self) -> None:
#         print(self.name)
#         print(self.idNumber)
    
#     def details(self) -> None:
#         print("My name is {}".format(self.name))
#         print("idNumber {}".format(self.idNumber))

# # child class ..
# class Employee(Person):

#     def __init__(self,name,idNumber,salary, post) -> None:
#         self.salary = salary 
#         self.post = post 

#         # call the Based class constructer ..
#         Person.__init__(self,name, idNumber)

#     def details(self) -> None:
#         print(super().details())
#         print("Post: {}".format(self.post))


# a = Employee("Shahid",12105824, 10000000, "Intern")
# a.display()
# a.details()


# # Polymorphism : Polymorphism is simply means many form at a time . it is override of the method ..

# class Bird:
#     def into(self):
#         print("There are Many Bird")

#     def flight(self) -> None: 
#         print(" Some Bird are Fly some are not")
    
# class Sparrow(Bird):
#     def flight(self) -> None:
#         print(" Sparrow is Flight ")

# class Ostrich(Bird):
#     def flight(self) -> None:
#         print(" Ostrich is Can not fly")


# obj_bird = Bird()
# obj_spa = Sparrow()
# obj_ost = Ostrich()

# obj_bird.into()
# obj_bird.flight()

# obj_spa.into()
# obj_spa.flight()

# obj_ost.into()
# obj_ost.flight()



# # Encapsulation: This is a main funcdmantal concept of the Object Oriented Programmig . Becuase '
# # it is describe the method and variable in one unit .This puts Restriction on accessing the variabke 
# #and method directly and can present accident modifying the data . anaccident objet 
# # only changed by the objec method , this is called the privte varaiable .

# class Base:

#     def __init__(self) -> None:
#         self.c = "GeeksforGeeks"
#         self.__c = "GeeksforGeeks"
    
#     def privateAccess(self) -> int: 
#         return self.__c

# # derived class ..
# class Child(Base):

#     def __init__(self) -> None:
        
#         super().__init__()
#         print(" Calling the Varaiable of the Base class")
#         print(self.privateAccess()) # get the AttributeError Becuase Private variable doenot inheritance
    

# base = Base()
# print(base.c)
# child = Child()
# print(child)



# #  Data Hiding and Object Priting ...
# # data hiding is the best for the private variable and not the acces the the direct  in the method , it use the by the direct the method ..
# class Test:
    
#     __hiddenVariable = 0;

#     def add(self, increment) -> None:
#         self.__hiddenVariable = +increment
#         print(self.__hiddenVariable)

# t = Test()

# t.add(2)
# t.add(10)

# print(t.__hiddenVariable) # get the error becuase hidden varaibel is not the use of the outsid eof the clas .


# # By the using the Hidden variable using some extran ways ..
# print(t._test__hiddenVariable) # get the hidden value of the object ..



# # Printing the Ojject ..
# # Printing objct Give the information of  the object . In Python it defualt __repr__ or __str__ method ..

# class Testing:

#     def __init__(self,a,b) -> None:
#         self.a = a
#         self.b = b 
    
#     def __repr__(self) -> None:
#         return " Test the String of the passing in the test a %s and B %s "% (self.a, self.b)
    
#     def __str__(self) -> None: 
#         return "Testing a%s b%s"% (self.a, self.b)


# tester = Testing(1234,5678)
# print(tester) # This call str ..
# print([tester]) # this call the __repr__


# #if  the __repr__ is no defined then __str__ method ois used  and if __str__ is not defined then it default used .
# class Testing2: 

#     def __init(self,a,b) -> None: 
#         self.a = a
#         self.b = b 

# tester2 = Testing2(1234, 5678)
# print(tester2)


# Inheritance in Python (OOP using the issubclass and isinstance method )
# issubset is a also method is avaible is set data type .

# class Person(object):
#     def __init__(self,name) -> None:
#         self.name = name 
    
#     def getName(self) -> str:
#         return self.name
    
#     def isEmpolye(self) -> bool:
#         return False 

# class Employe(Person): 
#     def isEmpolye(self) -> bool:
#         return True 

# emp = Person("geeks1") # return False 
# print(emp.getName(), emp.isEmpolye())

# emp2 = Employe("Geeks2")
# print(emp2.getName(), emp2.isEmpolye()) # return the True 


# # CHECK THE CLASS IS SUBCLASS OR NOT 
# print(issubclass(Employe, Person))
# print(issubclass(Person, Employe))

# #CHECK ISINSTANCE OF THE CLASS OR NOT \
# e = Employe("name")
# p = Person("name_person")

# print(isinstance(e, Person)) # return True 
# print(isinstance(p, Employe)) # return False 



# # HOW TO ACCES PAREMETER FROM THE SUPERCLASS INTO SUBCLASS BY TWO METHOD .
# # 1 ST METHOD USING THE PARENT CLASS ..

# class Base(object):
#     def __init__(self,a) -> None:
#         self.a = a

# class Derived(Base):

#     def __init__(self, a,b) -> None:
#         # by using the class Name .
#         Base.a = a
#         self.b = b 
    
#     def printAB(self) -> None:
#         print(Base.a, self.b)


# base = Derived(10,20)
# base.printAB()
# # BY USING SUPER CLASS ..

# class Boy(object):
#     def __init__(self,x) -> None:
#         self.x =x 

#     # def getName(arg):
#     #     pass

# class Name(Boy):

#     def __init__(self, x,y) -> None:
#          # 1 method to use the super method 
#         #  super(Name, self).__init__(x) # second method is : super().__intit(x)
#         super().__init__(x)
#         self.y = y
#         # super(Name, self).getName()
        
#     def printXY(self) -> None: 
#         print(self.x , self.y)

# name = Name(10,20)
# name.printXY()

# POLYMORPHISM IN PTYHON ..
# polymorphism is have many forms . it means is a one form has many form (but different parameter)

# print(len("name"))
# print(len([i for i in range(10)])) # here we use the len method to two time so there we use the lenmethod /


#  USE POLYMOR[HIME IN ] INHERITANCE ..

# def func(objects):
#     print(objects.info())
#     print(objects.flight())


# class Bird(object): # it automatically inheritance objecy class who is superclass or derived class.

#     def info(self) -> str:
#         return (" There are many Bird ")

#     def flight(self):
#         return (" Some Bird Can fly but some are not fly ")

# class Sparrow(Bird):
#     def flight(self):
#         # here we use the same method woho is inheritance in subclass abut here we use the other way ..
#         return (" Sparrow can fly") # first compiler is chaeck if flight is available or not in subclass if it not available in the sub class then the compiler find in the superclass and excute the programm

# class Ostrich(Bird):
#     def flight(self): 
#         return(" Ostrich Cann't fly")


# # using the itertor to print the polymorphism ..
# obj_bird = Bird()
# obj_spa = Sparrow()
# obj_ost = Ostrich() 
# obj_bird.info(), obj_bird.flight()

# for printer in (obj_bird,obj_spa, obj_ost):
#     print(printer.info())
#     print(printer.flight())

# 2ns using the polynorphism by function 
# (func(obj_bird))
# (func(obj_spa))
# (func(obj_ost))

# import polymor as py # import polymor file in class as us as object ..
# def student_Information(objects):
#     print(objects.college_name)
#     print(objects.name)
#     print(objects.id)
#     print(objects.section)

# class Student(py.Lpu):
#     def __init__(self, name, id, section) -> None:
#         super(Student, self).__init__(name, id, section)
    
#     # def setId(self, newId):
#     #     py.Lpu.setId(self,newId)
    
# student_name = input(" Enter Your Name :- ")
# student_id = input(" Enter Your Id :- ")
# student_section = input(" Enter Your Section :- ")

# newStudent = Student(student_name, student_id, student_section)
# # calling the function and printing the informatin 
# student_Information(newStudent)
# newStudent.setId(str(121058100))
# print(" new Id Generater is :- ", newStudent.id)






# Q...........................class and static method  in python
# All Variable are assigned in the class it called Class Variable and All Variable are Assigned in method it called Instance Method 

# class Spotify:

#     class_varaible = " Spotify" # this is class variable ..

#     def __init__(self, name, id) -> None:
#         self.name = name 
#         self.id = id  # this is instance variable 

# user = Spotify("shahid", 12100)
# second_user = Spotify("Ashad",2001)
# print(user.class_varaible)
# print(second_user.class_varaible) # get the class name by use the object 

# print(user.name)
# print(user.id)
# print("second user is \n")
# print(second_user.name)
# print(second_user.name)

# # change the class name of first user
# user.class_varaible = "Apple Music "
# print(" first User class name has been Changed ")
# print(user.class_varaible)
# print("Second User class Name is :- ")
# print(second_user.class_varaible)

# # class variable changed by class  .
# Spotify.class_varaible = " Spotify_Premimum"

# print(" First User Class Name : -")
# print(user.class_varaible)
# print(" second user class name ")
# print(second_user.class_varaible)


# Note : if you are changed class variable by using object then other object not changed becuase 
# every object are refererd to same class but differene memory location 
# so it not effiect , But Whr you chnaged the class vraibel name o
# by using the class name then it effect all object becuase all object are referd to same clas 



# 
#  @..................................class Method and static method ..
# class method access the class variable and state and change but not it is a object it treate by objet while static method not access the class 
# variable and modify them 
# class method by using @classmethod decorater and static method use @staticmethod decoretor 

''' ClassMethod : is a @classmethod decoretor function to bound with class not object of the class , it use to factory method 
it means similar to constructer, to bound with object .

Static Method : it means it a function @static method to also bound with class not object , it can access class or modify the class'''

# from datetime import date 

# class Person:

#     def __init__(self, name:str,year:int) -> None:
#         self.name = name
#         self.year = year 
    
#     # classmethod is use there 
#     @classmethod 
#     def fromBirthYear(cls,name,year):
#         return cls(name, date.today().year- year)
    

#     @staticmethod 
#     def isAdult(age:int) -> bool:
#         return age>18 

# person1 = Person("Shahid",12) #"" object of the Person class 
# person2 = Person.fromBirthYear("Shahid",2000) # this is a bound the  class not object of the Person 
# person2.year = 20000
# print(person1.year)
# print(person2.year)

# # get the type of the Person class
# print(type(person1))
# print(type(person2))

# #print the Static Method 
# print(Person.isAdult(22))



# Changing the Member in python ..
''' We should know when the changing the name of the class member : when we change the name of the class member it create another variable
(non static variabl) of object and it shadaow of those object '''

# class Spotify:
#     stream = " Spotify"

#     def __init__(self) -> None:
#         self.name = " Spotify"

# get_stream = Spotify() 
# print(" first Stream is : -", get_stream.stream)

# get_new_stream = Spotify()
# print(" new GEt_new_Stream is : ", get_new_stream.stream)

# # changing the name 
# get_stream.stream = " Apple Music "

# print(" chang the new Get_Stream is :- ", get_stream.stream)
# print(" new_get_stream is : ", get_new_stream.stream)


''' We Can Change The Class Member By Class Name ...'''

# Constructer in Python ...
''' Constructer is instilazation of object when the class is called. The task of 
constructer is initialize the data member when the class called ..


Two Type of Constructer : 1. Default Constructer ..
2. Parametrize Constructer ..'''

# class GeeksforGeeks:
#     def __init__(self) -> None:
#         self.name = "GeeksforGeeks"
    
#     def getName(self) -> str:
#         return self.name
# print("\nDefault Constructer is : ")
# objects = GeeksforGeeks()
# print(objects.getName())


# def getObject(args):
#     args.display()
#     args.calculate()
#     args.display()


# class Parameterize:
#     first=second=answer=0
#     def __init__(self, first, second) -> None:
# #         self.first = first 
# #         self.second = second
    
# #     def display(self) -> None:
# #         print(" First Variable is : ", self.first)
# #         print("Second Variable is : ", self.second)
# #         print(" Sum of the Two Variable is : ",self.answer)

# #     def calculate(self) -> None:
# #         self.answer = self.first+ self.second

# # print(" \nParametize Constructer is : ")        
# # param_object = Parameterize(100,200)
# # # param_object.display()
# # # param_object.calculate()
# # # param_object.display()
# # getObject(param_object)

# # DeConstructer in Python ...............

# ''' Deconstructer is a collection of Garbage collection of when the object not reference 
# to the memory location , in python is automatically collected garbage when the it called where 
# the c++ it is calleble '''

# class Name:
#     def __init__(self) -> None:
#         self.name = " My name  is World "
    
#     def __del__(self) -> None:
#         print(" DeConstructer is Calledable ...")

# # create the object o Name class 
# name = Name()
# print(" Calling the Name Class ..")

# # here the object automaically callable the deconstructer ..

# # USING THE SECOND WAT SIU G..
# class Spotify:
#     def __init__(self) -> None:
#         self.name = " Basic Name "

# class AppleMusic:
#     def __init__(self) -> None:
#         self.user = Spotify() # calling the Object of the Spotfy t=oi the class
#         print(" Memorize the Apple Music ") 
    
#     def __del__(self) -> None: 
#         print(" Deconstructer is DEclare in the Apple Music Class ")

# def function():
#     objects = AppleMusic() # Only Create The Flass and not usethe objec t..

# # here the ganbe collection is callable ..
# functions = function() # here we ue erty the function and uset he class of the function ..
# # here we usethe first class here but we use fucntion ...
# print(" Calling the Object is ...") 

# MetaProgramming or Metaclass in Python ......

''' Meta class is Create a class of class means it called class is instanec of metclass and 
object is instance of class , in python every built in class is metclass and when we use the 
metclass then it create a class and use by the object . in python we can create a metaclass 'by using the 
type method and in the type method if
1. if we passs 1 argument then it return the type of class of it argument 
2. if we pass three argument then it create a class by using 
    . class Name 
        inheritance class 
        dctionary of method and property '''

# def test_method(self):
#     print(" This is a test method ")

# class Base:
#     def my_fun(self):
#         print(" This is a my fun method ")


# # create the metaclass by using the type() emthod 
# Test = type('Test', (Base,), dict(varaible= " my_var", my_method= test_method))

# print(" Type of the test is :- ", type(Test))

# # create a object of class Test 
# obj_test = Test()
# print(" object of test is :- ", type(obj_test))

# obj_test.my_fun()
# obj_test.my_method()

# print(obj_test.varaible)


''' Create a Metclass using the MultiBase Inheritance class '''

# creating a abstarct class 
# abstract class is a class that store the function body and when the  subclass is define the parent class then we must be define the abstrcat class method else we get the error 

# from abc import ABC, abstractclassmethod, abstractmethod

# class Abstrcat:
#     @abstractmethod
#     def move(self): pass 
#     # now this is abstract class Method 

# class Name(Abstrcat):
    
#     def move(self):
#         print(" This is a Name class")

# class Second(Abstrcat):
    
#     def move(self):
#         print(" This is a Second Class Method ")

# # second Way to Define the Abstract class ..

# class Abstract(ABC):
#     # now we don't need to defin ethe abstractmetod decorator 
#     def move(self): pass 

# # now create another class and use the function in another class ..



# obj1 = Name()
# obj2 = Second()
# obj2.move()

# using the Abstract method ..

# from abc import ABC, abstractmethod
# class Person(ABC):
#     # @abstractmethod 
#     def name(self,name):
#         pass 
#     def age(self, age): pass 

# # using the absracft method /..
# class new_Person(Person):
#     def name(self, name="Shahid"):
#         self.name = name 
    
#     def age(self, age:int =20):
#         self.age = age 
    
#     # print the object ..
#     def __str__(self):
#         return (f"Your name is :- {self.name} and age is {self.age}")

# objects = new_Person()
# objects.name()
# objects.age()
# print(objects)


# using the Metaclass in python ..


# from functools import wraps
# def debug(function):
#     @wraps(function)
#     def wrapper(*args, **kwargs):
#         return function(*args, **kwargs)
#     return wrapper


# def debugmethod(cls):
#     for key, value in vars(cls).items():
#         if callable(value):
#             setattr(cls,key,debug(value))
#     return cls


# class Metclass(type):
#     def __new__(cls, clsname, bases, dictionary):
#         obj = super().__new__(cls, clsname, bases, dictionary)
#         obj = debugmethod(obj)
#         return obj 

# class New(metaclass= Metclass): pass

# class Calc(New):
#     def add(self,x:int,y:int):
#         return x+y

# obj = Calc()
# print(obj.add(10,20))


# Q.. class And Instance Attribute in pythom

''' class Attribiute of object is shared the object to each othe when there instanbce 
# object is not shared the object copy , it share the copy of every object '''

# class Name:
#     count = 0  # class Attribute 

#     def increase(self):
#         Name.count +=1 
    

# obj = Name()
# obj.increase()
# print(obj.count) # print 1
# obj.increase()
# print(obj.count) # print 2 



# class Instance:
#     def __init__(self) -> None:
#         self.name = "xyz"
#         self.salary = 4000 
    
#     def show(self):
#         print(self.name, self.salary)

# # var()  method return the attriute in the dictionary 
# # dir() method return teg directory of the object 

# def print_obj(objects:object):
#     objects.show()

# obj2 = Instance()
# print_obj(obj2)

# print(" Dictionary is :- ", vars(obj2))
# print(dir(obj2))
# if callable(obj2.show):
#     obj2.show()
# else: print("Function is Not callable ") # return the true if the function is callable ...

# def reverseddddd(sequence):
#     sequence_type = type(sequence)
#     print(sequence_type)
#     empty_sequence = sequence_type()
#     print(empty_sequence)

#     if sequence == empty_sequence:
#         return empty_sequence

#     rest = reverseddddd(sequence[2:])
#     print("here is :- ",rest)
#     final = sequence[0:1]
#     print("second is :- ",final)

#     final = rest+final
#     print(final)
#     return final 

# print(reverseddddd([10,20, 30 ,40]))
# print(reverseddddd("GeeksforGeeks"))

#User function Template for python3

 





