# num = 20
# if num % 2 == 0:
#     print("Num is Even")
# else:
#     print("Num is odd")
    
# num = 7
# if num <=1:
#     print("Num is not prime")
#     if num /2 === 0:

# num = 5
# fact = 1
# for i in range(1, num + 1):
#     fact *= i
# print(fact)

# str = "Kallu"
# rev = str[::-1]
# print(rev)
    
# str = "Kallu"
# rev = str[::-1]
# if(str == rev):
#     print("String is palindrome")   
# else:
#     print("String is not palindrome") 

# num = int(input("Enter num"))
# if(num<=1):
#     print("Num is not prime")
# else:
#     for i in range(2,num):
#         if num% i == 0:
#            print("Num is not prime")
#            break
#         else:
#             print("num is prime")

# num = int(input("Enter num"))
# a,b = 0,1
# for i in range(num):
#     print(a , end=" ")
#     a,b=b , a+b

# arr = [1,2,3,4,5,6]
# even = odd = 0
# for i in arr:
#     if i % 2 == 0:
#         print("Num is even")
#         even +=1
#     else:
#         print("Num is odd")
#         odd += 1
    
# class animal:
#        def speak(self):
#            print("Animals can speak")
# class dog(animal):
#         def bark(self):
#             print("Dog can bark")
#     d = dog()
#     d.speak()
#     d.bark()    

# str = input("Enter str").lower()
# vowels = 'aeiou'
# count = 0
# for ch in str:
#     if ch in vowels:
#         count +=1
# print("Count",count)        
        
#Count vowels
# vowels = 'AEIOUaeiou'
# count = 0
# name = "Kalyani"
# for i in name:
#     if i in vowels:
#       count +=1
# print("Count:",count)   

#fibonacii
# a = 0
# b = 1
# n=5
# for i in range(n):
#     print(a,end=" ")
#     a,b = b ,a+b
        
#Reverse a num
# n = 12345
# rev = 0
# while n > 0:
#     digit = n % 10
#     rev = rev * 10 + digit
#     n //= 10
# print(rev)

# Sum of digits
# n = 12345
# sum_digits = 0 
# while n > 0:
#     digit = n % 10
#     sum_digits += digit
#     n //= 10
# print(sum_digits)

# str = 'Kallu'
# rev = ''
# for i in str:
#     rev = i + rev
#     print("REV",rev)

# Large in array
# n = [1,2,3,4,8]
# large = 0
# for i in n:
#     if i>large:
#         large = i
# print(large)    

# Duplicate letters from strings
# str = "Programming"
# duplicate = ''

# for ch in str:
#     if ch not in duplicate:
#         if str.count(ch) > 1:
#          print(ch)
#     duplicate += ch

#anagram
# s1 = "listen"
# s2 = "silent"
# if sorted(s1) == sorted(s2):
#       print("Anagram")
# else:
#      print("Not anagram")

# piglatin.py
# word = 'Kalyani'
# vowels = "aeiou"

# for i in range(len(word)):
#     if word[i] in vowels:
#         result = word[i:] + word[:i] + "ay"
#         print("Result:", result)
#         break

# A router is receiving packets, one after another. Each arriving packet has some size. The router is able to repackage the 
# arriving packet together with the leftover of previous packets into one packet, but only if the size is a power of two 
# (1, 2, 4, 8, 16, ...).
# For each arriving packet:
# Add it to the leftover (if any).
# Find the largest power of 2 less than or equal to the total.
# That becomes the repackaged size.
# The leftover is reduced accordingly.
# Your task is to determine the largest repackaged size that the router can ever produce.
# Input Format:
# The first line contains an integer N, the number of packets.
# The next N lines contain integers, the sizes of the arriving packets.
# Output Format:
# Print a single integer — the maximum repackaged size.

n = int(input("Enter a num: "))
leftover = 0
max_size = 0

for _ in range(n):
    packet = int(input("Enter package size: "))
    total = leftover + packet

    power = 1
    while power * 2 <= total:
        power *= 2

    if power >= max_size:
        max_size = power

    leftover = total - power

print(max_size)