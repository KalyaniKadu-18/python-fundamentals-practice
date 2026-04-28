# Creating class and objects
# class Parent:
#     def __init__(self, name, rollNo):
#         self.name = name
#         self.rollNo = rollNo

#     def __str__(self):
#         return f"Name: {self.name}, Roll No: {self.rollNo}"

# ob1 = Parent("Kalyani", 1)
# print(ob1)

# Create a class BankAccount deposit(amount) withdraw(amount) display_balance()Create an object and perform deposit & withdrawal.
# class BankAccount:
#     def __init__(self, account_holder, balance):
#         self.account_holder = account_holder
#         self.balance = balance

#     def deposit(self, amount):
#         self.balance += amount
#         print("Deposited:", amount)

#     def withdraw(self, amount):
#         if amount <= self.balance:
#             self.balance -= amount
#             print("Withdrawn:", amount)
#         else:
#             print("Insufficient balance")

#     def display_balance(self):
#         print("Balance:", self.balance)


# # Object
# acc = BankAccount("Kalyani", 1000)
# acc.deposit(500)
# acc.withdraw(300)
# acc.display_balance()

# Create a class Employee with:attributes: name, salar increase_salary(percent) method display() Create object and increase salary by 10%.
# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary

#     def increase_salary(self, percent):
#         self.salary += self.salary * percent / 100

#     def display(self):
#         print("Name:", self.name)
#         print("Salary:", self.salary)


# # Object
# emp = Employee("Kalyani", 20000)
# emp.increase_salary(10)
# emp.display()

#Inheritance using constructor
# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
       
#     def Display(self):
#         print("Name: ",self.name)
#         print("Age: ",self.age)    
            
# class Student(Person):
#     def __init__(self,name,age,marks):
#          super().__init__(name,age)
#          self.marks = marks
    
#     def Display(self):
#         super().Display()
#         print("Marks: ",self.marks)     

# s1 = Student("Kalyani",21,99)
# s1.Display()
                   
#Overriding
# class Vehicle:
#     def __init__(self,name,type):
#          self.name = name
#          self.type = type
    
#     def Display(self):
#         print("Name of Vehicle is:",self.name)
#         print("Type of Vehicle is:",self.type)

# class Car(Vehicle):
#     def __init__(self, name, type,avg):
#         super().__init__(name, type)
#         self.avg = avg
    
#     def Display(self):
#         super().Display()
#         print("Avg of Car is:",self.avg) 
        
# c1 = Car("BMW","car",20)
# c1.Display()       


# Create a class Student with private __marks and methods to set and get marks.
# class Student:
#     def __init__(self,name,age):
#           self.name = name
#           self.age= age
#           self.__marks = 0
    
#     def setMarks(self,marks):
#         self.__marks = marks
        
#     def getMarks(self):
#         return self.__marks
        
# s1 = Student("Kalyani",20)
# s1.setMarks(98)
# print("Marks of student is:",s1.getMarks())

# class BankAcc:
#     def __init__(self,name,age,balance):
#         self.name = name
#         self.age = age
#         self.__balance = balance
        
#     def deposit(self,amount):
#         self.__balance += amount
#         print("Account Credited with", amount)
        
#     def withdraw(self,amount):
#         if amount <= self.balance:
#             self.__balance -= amount
#             print("Amount withdrawn",amount)
#         else:
#             print("Insufficient balance")
            
#     def showBalance(self):
#         print("Available balance in your acc is",self.__balance)            

# a1 = BankAcc("Kallu",20,2000)
# a1.deposit(9000)
# a1.showBalance() 

#Overloading using *args
# def add(*args):
#     return sum(args)
# print(add(2,3))
# print(add(2,3,4,5)) 

# Create a class Student with a method add_marks(*marks) to accept any number of marks and print their total.
# class Student:
#     def addMarks(self,*marks):
#         total = 0
#         for m in marks:
#             total += m
#         print("Total Marks",total)
            
# s = Student()
# s.addMarks(10,20)
# s.addMarks(20,30,40)
# s.addMarks(20,20.34,34)   

#**Kwargs - allows a function to take a named args 
# def StuData(**kwargs):
#     for key,value in kwargs.items():
#         print(key, ":" , value) 

# s1 = StuData(name="Kalyani",age=21,marks=89)             
        

#Polymorphism
# class cat:
#     def sound(self):
#         print("Meow!!")

# class Dog:
#     def sound(self):
#         print("Bark!!")
        
# for animal in (Dog(),cat()):
#     animal.sound()                                        

# class Shape:
#     def draw(self):
#         print("Can draw anything using this method")  
        
# class Circle:
#     def draw(self):
#         print("Drawing Cirlce")
        
# class Rectangle:
#     def draw(self):
#         print("Drawing Rectangle")
        
# for i in (Circle(),Rectangle()):
#     print(i.draw())        

#Abstraction
#abc(abstract base classes) ABC is the class in abc library
# from abc import ABC, abstractmethod

# class Animal(ABC):
#     @abstractmethod
#     def sound(self):
#         print("Can make sound")
        
# class Dog:
#     def sound(self):
#         print("Can bark!!")
        
# d = Dog()
# d.sound()            

#factorial 
def prime(n):
    if (n<=1):
        print("Num is not prime")
    else:
        while(n>1):
            if(n % 2 == 0):
                print("Num is not prime")
            else:
                print("Num is prime")
                break
prime(5)                

