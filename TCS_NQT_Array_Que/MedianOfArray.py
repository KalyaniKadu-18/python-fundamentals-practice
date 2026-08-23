arr = [4,5,2,6,23,5]
arr.sort()
n = len(arr)
if n % 2 == 0:
    median = (arr[n // 2 - 1] + arr[n // 2]) / 2
else:
    median = arr[n // 2]
print(median)        