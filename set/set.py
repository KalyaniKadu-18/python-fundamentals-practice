n = int(input("Enter the number of elements:"))
s = set()
for i in range (n):
    s.add(input("Enter elements: "))
    #Display
print("Elements of the set are:" ,s)
  #Length of set
print("Length of set is:" , len(s))
  #Count of digit, lowercase , uppercase 
digit = lowercase = uppercase = 0 
for ch in s:
    if ch.isdigit():
        digit+=1
    elif ch.islower():
        digit+=1          
    elif ch.isupper():
        digit+=1    
print("Count of digits:",digit)
print("count of lowercases:",lowercase)        
print("count of uppercases:",uppercase)        