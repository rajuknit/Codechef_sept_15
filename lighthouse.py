from collections import defaultdict
t=int(input())
while t>0:
  d=defaultdict(lambda:[])
  n=int(input())
  o=1
  while n>0:
   a,b=[int(x) for x in input().split()]
   d[a].append([b,o])
   o+=1
   n=n-1
  dd=[] 
  dd=sorted(d.items(),reverse=True)
  ee=[]
  ee=dd.copy()
  #print (dd)
  for i in range(len(dd)):
        pp=dd[i][0]
        qq=min(dd[i][1])
        dd[i]=[pp,qq]
        pp=ee[i][0]
        qq=max(ee[i][1])
        ee[i]=[pp,qq]
  #print(dd)
  #print(ee)

  #NW
  c1=1
  nw=[]
  nw=[dd[0][1][1]]
  min1=dd[0][1][0]
  for i in range(1,len(dd)):
    if dd[i][1][0]<min1:
               c1=c1+1
               nw.append(dd[i][1][1])
               min1=dd[i][1][0]
  #print(c1)


  #NE
  c2=1
  p=len(dd)
  ne=[]
  ne=[dd[p-1][1][1]]    
  min2=dd[p-1][1][0]    
      
  i=p-2
  while i>=0:
    if dd[i][1][0]<min2:
               c2=c2+1
               ne.append(dd[i][1][1])
               min2=dd[i][1][0]
    i=i-1           
 # print(c2)

  #SW
  c3=1
  sw=[]
  max1=ee[0][1][0]
  sw=[ee[0][1][1]]    
  for i in range(1,len(ee)):
    if ee[i][1][0]>max1:
               c3=c3+1
               sw.append(ee[i][1][1])
               max1=ee[i][1][0]
  #print(c3)



  #SE
  c4=1
  se=[]
  q=len(ee)
  max2=ee[q-1][1][0]
  se=[ee[q-1][1][1]]    
  i=q-2
  while i>0:
    if ee[i][1][0]>max2:
               c4=c4+1
               se.append(ee[i][1][1])
               max2=ee[i][1][0]
    i=i-1           
  #print(c4)

  c=min(c1,c2,c3,c4)
  if c==c1:
      print (c)
      for i in range(len(nw)):
         print(str(nw[i])+" NW")
               
  elif c==c2:
       print (c)
       for i in range(len(ne)):
         print(str(ne[i])+" NE") 

       
  elif c==c3:
        print (c)
        for i in range(len(sw)):
         print(str(sw[i])+" SW")     

        
  else:
       print (c)
       for i in range(len(se)):
         print(str(se[i])+" SE")
  t=t-1       
      
    
