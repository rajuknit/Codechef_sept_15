a=[4,6,3,2,1,7,8,10,2,3,4]
r=a[0]
min1=a[0]
max1=0
l1=0
l2=0
r2=0
r1=0
for i in range(1,len(a)):
    r=r^a[i]
    if r<min1:
        l1=i
        min1=r
    if r>max1 and i>=l1:
        r1=i
        max1=r
print (l1)
print (r1)
    
