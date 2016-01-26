t=int(input())
while t>0:
    n=int(input())
    a=[]
    for i in range(n):
        c,d=[int(x) for x in input().split()]
        a.append([c,d])
    mny=a[0][1]
    mxy=a[0][1]
    i1=0
    #min y with min x
    i2=0
    #max y with max x
    i3=0
    #min y with max x
    i4=0
    #max y with min x
    t1=a[0][0]
    t2=a[0][0]
    t3=a[0][0]
    t4=a[0][0]
    for i in range(n):
        #min y
        if mny>=a[i][1]:
            if mny==a[i][1]:
                # min x
                if t1>a[i][0]:
                    t1=a[i][0]
                    i1=i
                #max x    
                elif t3<a[i][0]:
                    t3=a[i][0]
                    i3=i
            else:
                t1=a[i][0]
                t3=a[i][0]
                mny=a[i][1]
                i1=i
                i3=i
                
        #max y       
        if mxy<=a[i][1]:
            if mxy==a[i][1]:
                #max x
                if t2<a[i][0]:
                    t2=a[i][0]
                    i2=i
                #min x    
                elif t4>a[i][0]:
                    t4=a[i][0]
                    i4=i    
            else:
                t2=a[i][0]
                t4=a[i][0]
                mxy=a[i][1]
                i2=i
                i4=i

                
    #print (str(i1+1) +" "+str(i2+1)+" "+str(i3+1) +" "+str(i4+1))
    mnx=a[0][0]
    mxx=a[0][0]
    for i in range(n):
        if mnx>a[i][0]:
            mnx=a[i][0]
        if mxx<a[i][0]:
            mxx=a[i][0]

    #answer section       
    if mnx==a[i1][0]:
        print(1)
        print(str(i1+1)+" NE")
    
    elif mxx==a[i2][0]:
        print(1)
        print(str(i2+1)+" SW")
    
    elif mxx==a[i3][0]:
        print(1)
        print(str(i3+1)+" NW")
    elif mnx==a[i4][0]:
        print(1)
        print(str(i4+1)+" SE")
        
    else:
        if a[i2][0]>a[i1][0]:
            print(2)
            print(str(i2+1)+" SW")
            print(str(i1+1)+" NE")
        else:
            print(2)
            print(str(i4+1)+" SE")
            print(str(i3+1)+" NW")
    t=t-1
"""  
        elif a[i2][0]<a[i1][0]:
            print(2)
            print(str(i2+1)+" SE")
            print(str(i1+1)+" NW")
        elif a[i4][0]>a[i4][0]:
            print(2)
            print(str(i4+1)+" SW")
            print(str(i4+1)+" NE")
        elif a[i4][0]<a[i4][0]:
            print(2)
            print(str(i4+1)+" SE")
            print(str(i3+1)+" NW")
"""     
"""
elif mxx==a[i1][0]:
        print(1)
        print(str(i1+1)+" NW")
elif mnx==a[i2][0]:
        print(1)
        print(str(i2+1)+" SE")
            
elif mnx==a[i3][0]:
        print(1)
        print(str(i3+1)+" NE")
   
elif mxx==a[i4][0]:
        print(1)
        print(str(i4+1)+" SW")
"""        
