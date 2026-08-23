def SecSmall():
    nums = [2,8,3,9,5,3,7,5,8]
    small = nums[0]
    secsmall = nums[0]
    for i in nums:
        if i < small:
            secsmall = small
            small = i
        elif i < secsmall and i != small:
             secsmall = i
    print(secsmall)
SecSmall()    
             
                