arr = [5,2,6,8,0,3,6,4,7]
for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        if arr[i] < arr[j]:
            arr[i],arr[j] = arr[j],arr[i]
print(arr)            
# arr.sort(reverse = true) for optimized solution
