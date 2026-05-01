def my_range(start,stop,step):
    while start<stop:
        yield start
        start += step
        
start = int(input("Enter start value: "))
stop = int(input("Enter stop value: "))
step = int(input("Enter step value: "))

for i in range(start,stop,step):
    print("\n Generated range is:" , i , end="")        