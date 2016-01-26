def dfs(a,cn,i,j,k):
    if i<0 or j<0 or i>=n or j>=m:
        return
    if cn[i][j]!=0:
        return
    if a[i][j]=='o':
        h[k]+=1
        cn[i][j]=k
        dfs(a,cn,i+1,j,k)
        dfs(a,cn,i,j+1,k)
        dfs(a,cn,i-1,j,k)
        dfs(a,cn,i,j-1,k)
    return    

t=int(input())
h=[0]*200000
while t>0:
    n,m=[int(x) for x in input().split()]
    a=[]
    cn=[]
    d=[0]*m
    for i in range(n):
            b=input()
            a.append(b)
            cn.append(d)
            
    c=1
    for i in range(n):
        for j in range(m):
            
            if cn[i][j]==0 and a[i][j]=='o':
                h[c]=0
                
                dfs(a,cn,i,j,c)
                c+=1
    for i in range(n):
        for i in range(m):
            print(cn[i][j],end=" ")
        print()
    for i in range(c):
        print(h[i])
    t=t-1
