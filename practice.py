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
class BankAccount:
    def __init__(self,amount,balance):
        self.amount = amount
        self.balance = balance   
        