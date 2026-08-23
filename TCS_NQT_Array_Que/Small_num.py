def SmallNum():
    nums = [1, 2, 6, 4, 9, 3, 5]
    small = nums[0]

    for i in nums:
        if i < small:
            small = i

    print(small)

SmallNum()