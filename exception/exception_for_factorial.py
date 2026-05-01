def factorial_exception(n):
    if n<0 :
        raise Exception("Invalid input")
    factorial = 1
    for i in range(1,n+1):
        factorial *= i
    return factorial

try:
    num = int(input("Enter number to find the factorial:"))
    print("Fatorial of the number is:" , factorial_exception(num))  
except Exception as e:
    print(e)    