def reverse_string(s):
    words = s.split()
    result = [word[::-1] for word in words]
    return " ".join(result)
string = input("Enter the string:")
print(reverse_string(string))