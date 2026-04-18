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