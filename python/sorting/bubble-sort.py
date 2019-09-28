a = [9,8,7,6,5,4,3,2,1]

print(a)

for i in range(len(a)-1,0,-1):
    for x in range(i):
        if a[x] > a[x+1]:
            a[x], a[x+1] = a[x+1], a[x]

print(a)