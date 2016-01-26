import random
f=open("xor4.txt",'w')
s=""
for i in range(10):
    s=s+str(random.randint(10**8,10**9))+" "
f.write(s)    
f.close()
