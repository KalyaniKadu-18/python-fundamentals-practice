nums = [1,4,7,3,5,3,8,10]
large = nums[0]
for i in nums:
    if i > large:
        large = i
print(large)