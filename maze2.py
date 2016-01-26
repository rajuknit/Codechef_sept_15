def validation(rr,cc,r,c,a,map1):
    #print(str(rr)+" "+str(cc)+" "+str(r)+" "+str(c))
    if cc>=c or cc<=-1 or rr>=r or rr<=-1:
        return 0
    if map1[rr][cc]=="#":
        return 0
    if a[rr][cc]==1:
        return 0
    return 1
    



def floodfill(x, y,r,c,a,map1):
    theStack = [ (x, y) ]
    cn=0
    while len(theStack) > 0:
        x, y = theStack.pop()
        cn=cn+1
        a[x][y]=1
        if validation(x,y+1,r,c,a,map1)==1:
            theStack.append( (x, y + 1) )  # down
            a[x][y+1]=1
        if validation(x+1,y,r,c,a,map1)==1:    
          theStack.append( (x + 1, y) )  # right
          a[x+1][y]=1
        if validation(x-1,y,r,c,a,map1)==1:  
          theStack.append( (x - 1, y) )  # left
          a[x-1][y]=1
        if validation(x,y-1,r,c,a,map1)==1:
          theStack.append( (x, y - 1) )  # up
          a[x][y-1]=1
    return cn     

#f=open("game.txt",'r')
t=int(input())
while t>0:
    r,c=[int(x) for x in  input().split()]
    map1=[]
    a=[]
    for i in range(r):
        map1.append(input())
        #map1.append(f.readline())
        a.append([0]*c)
    oo=0
    la=[]
    avg=0
    for i in range(r):
        for j in range(c):
            if map1[i][j]=='o':
              oo+=1  
              if a[i][j]==0 :
                kk=floodfill(i,j,r,c,a,map1)
                la.append(kk)
                avg+=kk
    #for i in range(r):
    #    print(a[i])
    cnt=la.pop(0)
    avg=avg-cnt
    lc=len(la)
    #print(cnt)
    #print(la)
    if lc==0:
        print("1.000000")
    else:
        
        tot=avg
        avg=avg/lc
        #print("cnt "+str(cnt))
        #print("oo "+str(oo))
        #print("tot "+str(tot))
        #print("avg "+str(avg))
        ans=cnt/oo
        xx=tot/oo
        #print("xx "+str(xx))
        #print(ans)
        ans+=(2)*(cnt/(oo-(avg)))*xx
        for i in range(1,lc):
            xx=xx*((tot-(avg*i))/(oo-(avg*i)))
            ans+=(2+i)*(cnt/(oo-((i+1)*avg)))*xx
            #print("xxi "+str(xx))
        print(ans)  
        
        
    t=t-1


"""
if (k==lc-1 or (k+1==i and j==i)) and g==1:
                              g=0
                              pp=pp*((oo-cnt-vv)/(oo-vv))
                              
                              vv+=la[k]
                              
                            else:
"""
"""
 ans=cnt/oo
        for i in range(lc):
                b=i+2
                ll=0
                for j in range(lc):
                    pp=(la[j]/oo)
                    print("pp1 "+str(pp))
                    g=1
                    vv=la[j]
                    ii=0
                    qq=0
                    for k in range(lc):
                        #if ii==i:
                        #    break
                        if k!=j:
                              ii=ii+1
                              if oo>vv:
                               pp=pp*(la[k]/(oo-vv))
                               print("pp "+str(pp))
                               vv+=la[k]
                              
                    pp=pp*(cnt/(oo-vv))          
                    print("pp1 "+str(pp))        
                    ll+=pp
                print("ll "+str(ll))
                b=b*ll
                #b=b*(cnt/(oo-vv))
                print("b "+str(b))
                ans+=b
                print("ans "+str(ans))
        print(ans)
"""       
