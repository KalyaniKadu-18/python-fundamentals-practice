S = input("Enter the string : ")
result = " "
for i in range(0, len(S)-1, 2):
    result += S[i+1] + S[i]
if len(S) % 2 != 0:
    result += S[-1]
print("The strings after changing add and even positions :",result)    
