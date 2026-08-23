#Creating a file
# file = open("newDemo.txt","x")
# file.write("Creating a new file using x mode")
# file.close()

# opening and writing to a file 
# file = open("Demo.txt","w")
# file.write("I am Kalyani")
# file.close()

#opening and reading to a file 
# file = open("Demo.txt","r")
# file.read()
# file.readline()
# file.readlines()
# file.close()
# print("File opened successfully")

#opening and appending to a file 
# file = open("Demo.txt","a")
# file.write("\n New line added")
# file.writelines("\n Adding new lines")
# file.close()

# with open("Demo.txt","w") as file:
    # file.write("Using with keyword")
    
#exception handling 
# try:
#     with open("Demo.txt","r") as f:
#         f.read()
#         f.close()
#         print("File founded successfully")
# except FileNotFoundError:
#     print("File not found")
             
#File operations (delete ,rename)
# os.rename("Demo.txt","newDemo.txt")
# os.remove("newDemo.txt") 

#chk if file exists
# print(os.path.exists("Demo.txt"))

#Get file info
# print(os.path.getsize("Demo.txt"))
# print(os.listdir())