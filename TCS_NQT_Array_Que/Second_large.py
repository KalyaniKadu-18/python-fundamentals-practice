def SecLarge():
    nums = [2,5,1,7,3,8,4,9]
    large = nums[0]
    secLarge = nums[0]
    for i in nums:
        if i > large:
            secLarge = large
            large = i
        elif i > secLarge and i != large:
            secLarge = i
    print(secLarge)
SecLarge()                
            
    