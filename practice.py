# Q1 Write a program to check whether a number is prime using a function.
# def Prime(n):
#     if n <=1:
#         print("Num is not prime")
#     else:
#         while(n > 1):
#             if n % 2 == 0:
#                 print("num is not prime")
#             else:
#                 print("Num is prime")
#             break
# Prime(10)            

# Q2 Create a class Student with __init__ and __str__ to store and display name and marks.
# class Student:
#     def __init__(self,name,marks):
#         self.name = name
#         self.marks = marks
    
#     def __str__(self):
#         return self.name
    
#     def Display(self):
#         print("Marks of students are:",self.marks)
    
# s1 = Student("Kalyani",90)
# print(s1)  
# s1.Display()

# Q3 Write a program to find factorial using recursion.
# def factorial(n):
#     if n == 1:
#         return 1
#     else:
#        return n *factorial(n-1)
# print(factorial(5))

# Q4 Create a class Rectangle with methods to calculate area and perimeter.
# class Rectangle:
#     def __init__(self,length,breadth):
#         self.length = length
#         self.breadth = breadth
        
    
#     def area(self):
#         return self.length * self.breadth
    
#     def Perimeter(self):
#         return 2 *(self.length + self.breadth)
        
#     def Display(self):     
#         print("Area is :" , self.area())
#         print("Perimeter is:",self.Perimeter())
        
# r1 = Rectangle(10,20)
# r1.Display()

# Q5 Write a program to check whether a string is a palindrome without slicing.
# str = 'madam'
# rev = ""
# for i in str:
#     rev = i + rev
# if str == rev:
#         print("String is palindrome")
# else:
#         print("Not Plaindrome")
            
# Q6 Create a class BankAccount with:deposit() withdraw() Also handle invalid withdrawal using exception handling.
# class BankAccount:
#     def __init__(self,amount,balance=0):
#         self.amount = amount
#         self.balance = balance   
        
#     def deposit(self,amount):
#             self.balance += amount
#             print("You deposited:",amount)
            
#     def withdraw(self,amount):
#         try:
#             if amount > self.balance:
#                 raise Exception("Insufficient balance")
#             self.balance -= amount
#             print("Withdrawn:" ,amount)
#             print("Balance",self.balance)
#         except Exception as e:
#             print(e)
            
# customer = BankAccount(100)
# customer.deposit(1000)
# customer.withdraw(20)
# print(customer) 

# Q7 Write a program to count frequency of characters in a string using dictionary.
# s = 'Ashwini'
# freq = {}
# for ch in  s:
#     if ch in freq:
#         freq[ch] +=1
#     else:
#         freq[ch] = 1
# print(freq)

# Q8 Demonstrate inheritance: Class Person Class Employee (inherits Person) Display employee details.
# class Person:
#     def __init__(self, name, dept):
#         self.name = name
#         self.dept = dept

#     def Display(self):
#         print("Name:", self.name)
#         print("Department:", self.dept)


# class Employee(Person):
#     def __init__(self, name, dept, salary):
#         super().__init__(name, dept)   # correct call
#         self.salary = salary
        
#     def Display(self):
#         super().Display()
#         print("Salary:", self.salary)


# s1 = Employee('Kalyani', 'IT', 200000)   # create Employee object
# s1.Display()

# Q9 Create a class that overloads + operator using __add__ to add two objects.
# class C1:
#     def __init__(self,a,b):
#         self.a = a
#         self.b = b
    
#     def Display(self):
#         print("Value of a:",self.a)
#         print("Value of b", self.b)
            
# class C2(C1):
#     def __add__(self,other):
#         return C2(self.a +other.a,self.b+other.b)
  
#     def Display(self):
#         print("Value of a:",self.a)
#         print("Value of b", self.b)

# object = C2(10,20)
# object2 = C2(5,5)
# object3 = object + object2
# object3.Display()

# Q10 Create an abstract class Shape with method area() and implement it in:Circle Square
from abc import ABC , abstractmethod

