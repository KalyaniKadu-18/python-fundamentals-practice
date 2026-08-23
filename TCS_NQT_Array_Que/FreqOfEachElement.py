arr = [8,4,6,3,7,2,5]
frq = {}
for i in arr:
    if i in frq:
        frq[i] += 1
    else:
        frq[i] = 1
print(frq)