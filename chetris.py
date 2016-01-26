import random
a=[14]*15
g=[0]*15

while(1):
    inp=input()
    if inp=="Game over":
        break
    s=[]
    s=inp.split()
    typ=int(s[0])
    fig=int(s[1])
    if typ==2:
        rt=s[2]
    if typ==2:
        if fig==1:
            if rt=="a":
               max1=a[0]
               ii=0
               for i in range(len(a)-3):
                    if a[i]>max1:
                        max1=a[i]
                        ii=i
               r=ii+1   
               #r=random.randint(1,12)
               x=min(a[r-1],a[r],a[r+1],a[r+2])
               c=x+1
               
               
               a[r-1]=x-1
               a[r]=x-1
               a[r+1]=x-1
               a[r+2]=x-1
               v=15-c
               g[v]+=4
               for i in range(14,-1,-1):
                   if g[i]==15:
                        for j in range(i,14):
                           g[i]=g[i+1]
                        a[r-1]-=1
                        a[r]-=1
                        a[r+1]-=1
                        a[r+2]-=1
                        
               
               print("a "+str(c)+" "+str(r))
            elif rt=="b":
                max1=a[0]
                ii=0
                for i in range(len(a)):
                    if a[i]>max1:
                        max1=a[i]
                        ii=i
                r=ii+1
                #r=random.randint(1,15)
                c=a[r-1]+1
                a[r-1]=a[r-1]-4
                v=15-c
                g[v]+=1
                g[v+1]+=1
                g[v+2]+=1
                g[v+3]+=1
                for i in range(14,-1,-1):
                   if g[i]==15:
                        for j in range(i,14):
                           g[i]=g[i+1]
                        a[r-1]-=4
                        
                
                print("b "+str(c)+" "+str(r))    
        elif fig==2:
            if rt=="a":
                max1=a[0]
                ii=0
                for i in range(len(a)-2):
                    if a[i]>max1:
                        max1=a[i]
                        ii=i
                r=ii+1
                #r=random.randint(1,13)
                x=min(a[r-1],a[r],a[r+1])
                c=x+1
                
                a[r-1]=x-2
                a[r]=x-1
                a[r+1]=x-1
                v=15-c
                g[v]+=3
                g[v+1]+=1
                for i in range(14,-1,-1):
                   if g[i]==15:
                        for j in range(i,14):
                           g[i]=g[i+1]
                        a[r-1]-=1
                        a[r]-=1
                        a[r+1]-=1

                print("a "+str(c)+" "+str(r))
            elif rt=="b":
                max1=a[0]
                ii=0
                for i in range(len(a)-1):
                    if a[i]>max1:
                        max1=a[i]
                        ii=i
                r=ii+1
                #r=random.randint(1,14)
                x=min(a[r-1],a[r])
                c=x+1
                
                a[r-1]=x-1
                a[r]=x-3
                v=15-c
                g[v]+=2
                g[v+1]+=1
                g[v+2]+=1
                for i in range(14,-1,-1):
                   if g[i]==15:
                        for j in range(i,14):
                           g[i]=g[i+1]
                        a[r-1]-=1
                        a[r]-=1
                        
                print("b "+str(c)+" "+str(r))
            elif rt=="c":
               max1=a[0]
               ii=0
               for i in range(len(a)-1):
                    if a[i]>max1:
                        max1=a[i]
                        ii=i
               r=ii+1
               #r=random.randint(1,14)
               x=min(a[r-1],a[r])
               c=x+1
               a[r-1]=x-3
               a[r]=x-3
               v=15-c
               g[v]+=1
               g[v+1]+=1
               g[v+2]+=2
               for i in range(14,-1,-1):
                   if g[i]==15:
                        for j in range(i,14):
                           g[i]=g[i+1]
                        a[r-1]-=1
                        a[r]-=1
                        
               print("c "+str(c)+" "+str(r))
            elif rt=="d":
                max1=a[0]
                ii=0
                for i in range(len(a)-2):
                    if a[i]>max1:
                        max1=a[i]
                        ii=i
                r=ii+1
                #r=random.randint(1,13)
                x=min(a[r-1],a[r],a[r+1])
                c=x+1
                a[r-1]=x-2
                a[r]=x-2
                a[r+1]=x-2
                v=15-c
                g[v]+=1
                g[v+1]+=3
                for i in range(14,-1,-1):
                   if g[i]==15:
                        for j in range(i,14):
                           g[i]=g[i+1]
                        a[r-1]-=1
                        a[r]-=1
                        a[r+1]-=1

                print("d "+str(c)+" "+str(r))
        elif fig==3:
            if rt=="a":
                 max1=a[0]
                 ii=0
                 for i in range(len(a)-2):
                    if a[i]>max1:
                        max1=a[i]
                        ii=i
                 r=ii+1
                 #r=random.randint(1,13)
                 x=min(a[r-1],a[r],a[r+1])
                 c=x+1
                 a[r-1]=x-1
                 a[r]=x-1
                 a[r+1]=x-2

                 v=15-c
                 g[v]+=3
                 g[v+1]+=1
                 for i in range(14,-1,-1):
                   if g[i]==15:
                        for j in range(i,14):
                           g[i]=g[i+1]
                        a[r-1]-=1
                        a[r]-=1
                        a[r+1]-=1
                 print("a "+str(c)+" "+str(r))
            elif rt=="b":
                max1=a[0]
                ii=0
                for i in range(len(a)-1):
                    if a[i]>max1:
                        max1=a[i]
                        ii=i
                r=ii+1
                #r=random.randint(1,14)
                x=min(a[r-1],a[r])
                c=x+1
                a[r-1]=x-3
                a[r]=x-1
                v=15-c
                g[v]+=2
                g[v+1]+=1
                g[v+2]+=1
                for i in range(14,-1,-1):
                   if g[i]==15:
                        for j in range(i,14):
                           g[i]=g[i+1]
                        a[r-1]-=1
                        a[r]-=1
                print("b "+str(c)+" "+str(r))
            elif rt=="c":
                 max1=a[0]
                 ii=0
                 for i in range(len(a)-2):
                    if a[i]>max1:
                        max1=a[i]
                        ii=i
                 r=ii+1
                 #r=random.randint(1,13)
                 x=min(a[r-1],a[r],a[r+1])
                 c=x+1
                 a[r-1]=x-2
                 a[r]=x-2
                 a[r+1]=x-2
                 v=15-c
                 g[v]+=1
                 g[v+1]+=3
                 for i in range(14,-1,-1):
                   if g[i]==15:
                        for j in range(i,14):
                           g[i]=g[i+1]
                        a[r-1]-=1
                        a[r]-=1
                        a[r+1]-=1
                 print("c "+str(c)+" "+str(r))
            elif rt=="d":
                 max1=a[0]
                 ii=0
                 for i in range(len(a)-1):
                    if a[i]>max1:
                        max1=a[i]
                        ii=i
                 r=ii+1
                # r=random.randint(1,14)
                 x=min(a[r-1],a[r])
                 c=x+1
                 
                 a[r-1]=x-3
                 a[r]=x-3
                 v=15-c
                 g[v]+=1
                 g[v+1]+=1
                 g[v+1]+=2
                 
                 for i in range(14,-1,-1):
                   if g[i]==15:
                        for j in range(i,14):
                           g[i]=g[i+1]
                        a[r-1]-=1
                        a[r]-=1
                        
                 print("d "+str(c)+" "+str(r))
        elif fig==4:
                max1=a[0]
                ii=0
                for i in range(len(a)-1):
                    if a[i]>max1:
                        max1=a[i]
                        ii=i
                r=ii+1
                #r=random.randint(1,14)
                x=min(a[r-1],a[r])
                c=x+1
                a[r-1]=x-2
                a[r]=x-2
                v=15-c
                g[v]+=2
                g[v+1]+=2
                for i in range(14,-1,-1):
                   if g[i]==15:
                        for j in range(i,14):
                           g[i]=g[i+1]
                        a[r-1]-=1
                        a[r]-=1
                               
                print("a "+str(c)+" "+str(r))
        elif fig==5:
            if rt=="a":
                max1=a[0]
                ii=0
                for i in range(len(a)-2):
                    if a[i]>max1:
                        max1=a[i]
                        ii=i
                r=ii+1
                #r=random.randint(1,13)
                x=min(a[r-1],a[r],a[r+1])
                c=x+1
                a[r-1]=x-1
                a[r]=x-2
                a[r+1]=x-2
                v=15-c
                g[v]+=2
                g[v+1]+=2
                for i in range(14,-1,-1):
                   if g[i]==15:
                        for j in range(i,14):
                           g[i]=g[i+1]
                        a[r-1]-=1
                        a[r]-=1
                        a[r+1]-=1
                print("a "+str(c)+" "+str(r))
            elif rt=="b":
                max1=a[0]
                ii=0
                for i in range(len(a)-1):
                    if a[i]>max1:
                        max1=a[i]
                        ii=i
                r=ii+1
                #r=random.randint(1,14)
                x=min(a[r-1],a[r])
                c=x+1
                a[r-1]=x-3
                a[r]=x-2
                v=15-c
                g[v]+=1
                g[v+1]+=2
                g[v+1]+=1
                for i in range(14,-1,-1):
                   if g[i]==15:
                        for j in range(i,14):
                           g[i]=g[i+1]
                        a[r-1]-=1
                        a[r]-=1
                        
                print("b "+str(c)+" "+str(r))

        elif fig==6:
            if rt=="a":
                max1=a[0]
                ii=0
                for i in range(len(a)-2):
                    if a[i]>max1:
                        max1=a[i]
                        ii=i
                r=ii+1
                #r=random.randint(1,13)
                
                x=min(a[r-1],a[r],a[r+1])
                c=x+1
                a[r-1]=x-1
                a[r]=x-2
                a[r+1]=x-1
                v=15-c
                g[v]+=3
                g[v+1]+=1
                for i in range(14,-1,-1):
                   if g[i]==15:
                        for j in range(i,14):
                           g[i]=g[i+1]
                        a[r-1]-=1
                        a[r]-=1
                        a[r+1]-=1
                print("a "+str(c)+" "+str(r))

            elif rt=="b":
                max1=a[0]
                ii=0
                for i in range(len(a)-1):
                    if a[i]>max1:
                        max1=a[i]
                        ii=i
                r=ii+1
                #r=random.randint(1,14)
                x=min(a[r-1],a[r])
                c=x+1
                a[r-1]=x-3
                a[r]=x-2
                v=15-c
                g[v]+=1
                g[v+1]+=2
                g[v+2]+=1
                for i in range(14,-1,-1):
                   if g[i]==15:
                        for j in range(i,14):
                           g[i]=g[i+1]
                        a[r-1]-=1
                        a[r]-=1
                        
                print("b "+str(c)+" "+str(r))

            elif rt=="c":
                max1=a[0]
                ii=0
                for i in range(len(a)-2):
                    if a[i]>max1:
                        max1=a[i]
                        ii=i
                r=ii+1
                #r=random.randint(1,13)
                
                x=min(a[r-1],a[r],a[r+1])
                c=x+1
                a[r-1]=x-2
                a[r]=x-2
                a[r+1]=x-2
                v=15-c
                g[v]+=1
                g[v+1]+=3
                for i in range(14,-1,-1):
                   if g[i]==15:
                        for j in range(i,14):
                           g[i]=g[i+1]
                        a[r-1]-=1
                        a[r]-=1
                        a[r+1]-=1
                print("c "+str(c)+" "+str(r))

            elif rt=="d":
                max1=a[0]
                ii=0
                for i in range(len(a)-1):
                    if a[i]>max1:
                        max1=a[i]
                        ii=i
                
                #r=random.randint(1,14)
                x=min(a[r-1],a[r])
                c=x+1
                
                a[r-1]=x-2
                a[r]=x-3
                v=15-c
                g[v]+=1
                g[v+1]+=2
                g[v+2]+=1
                for i in range(14,-1,-1):
                   if g[i]==15:
                        for j in range(i,14):
                           g[i]=g[i+1]
                        a[r-1]-=1
                        a[r]-=1
                    
                print("d "+str(c)+" "+str(r))
        elif fig==7:
            if rt=="a":
                max1=a[0]
                ii=0
                for i in range(len(a)-2):
                    if a[i]>max1:
                        max1=a[i]
                        ii=i
                r=ii+1
                #r=random.randint(1,13)
                x=min(a[r-1],a[r],a[r+1])
                c=x+1
                a[r-1]=x-2
                a[r]=x-2
                a[r+1]=x-1
                v=15-c
                g[v]+=2
                g[v+1]+=2
                for i in range(14,-1,-1):
                   if g[i]==15:
                        for j in range(i,14):
                           g[i]=g[i+1]
                        a[r-1]-=1
                        a[r]-=1
                        
                print("a "+str(c)+" "+str(r))
            elif rt=="b":
                max1=a[0]
                ii=0
                for i in range(len(a)-1):
                    if a[i]>max1:
                        max1=a[i]
                        ii=i
                r=ii+1
                #r=random.randint(1,14)
                x=min(a[r-1],a[r])
                c=x+1
                a[r-1]=x-2
                a[r]=x-3
                v=15-c
                g[v]+=1
                g[v+1]+=2
                g[v+2]+=1
                for i in range(14,-1,-1):
                   if g[i]==15:
                        for j in range(i,14):
                           g[i]=g[i+1]
                        a[r-1]-=1
                        a[r]-=1
                    
                print("b "+str(c)+" "+str(r))

    elif typ==1:
        if fig==1:
            rt=random.choice("ab")
            if rt=="a":
               max1=a[0]
               ii=0
               for i in range(len(a)-3):
                    if a[i]>max1:
                        max1=a[i]
                        ii=i
               r=ii+1   
               #r=random.randint(1,12)
               x=min(a[r-1],a[r],a[r+1],a[r+2])
               c=x+1
               
               
               a[r-1]=x-1
               a[r]=x-1
               a[r+1]=x-1
               a[r+2]=x-1
               v=15-c
               g[v]+=4
               for i in range(14,-1,-1):
                   if g[i]==15:
                        for j in range(i,14):
                           g[i]=g[i+1]
                        a[r-1]-=1
                        a[r]-=1
                        a[r+1]-=1
                        a[r+2]-=1
                        
               
               print("a "+str(c)+" "+str(r))
            elif rt=="b":
                max1=a[0]
                ii=0
                for i in range(len(a)):
                    if a[i]>max1:
                        max1=a[i]
                        ii=i
                r=ii+1
                #r=random.randint(1,15)
                c=a[r-1]+1
                a[r-1]=a[r-1]-4
                v=15-c
                g[v]+=1
                g[v+1]+=1
                g[v+2]+=1
                g[v+3]+=1
                for i in range(14,-1,-1):
                   if g[i]==15:
                        for j in range(i,14):
                           g[i]=g[i+1]
                        a[r-1]-=4
                        
                
                print("b "+str(c)+" "+str(r))    
        elif fig==2:
            rt=random.choice("abcd")
            if rt=="a":
                max1=a[0]
                ii=0
                for i in range(len(a)-2):
                    if a[i]>max1:
                        max1=a[i]
                        ii=i
                r=ii+1
                #r=random.randint(1,13)
                x=min(a[r-1],a[r],a[r+1])
                c=x+1
                
                a[r-1]=x-2
                a[r]=x-1
                a[r+1]=x-1
                v=15-c
                g[v]+=3
                g[v+1]+=1
                for i in range(14,-1,-1):
                   if g[i]==15:
                        for j in range(i,14):
                           g[i]=g[i+1]
                        a[r-1]-=1
                        a[r]-=1
                        a[r+1]-=1

                print("a "+str(c)+" "+str(r))
            elif rt=="b":
                max1=a[0]
                ii=0
                for i in range(len(a)-1):
                    if a[i]>max1:
                        max1=a[i]
                        ii=i
                r=ii+1
                #r=random.randint(1,14)
                x=min(a[r-1],a[r])
                c=x+1
                
                a[r-1]=x-1
                a[r]=x-3
                v=15-c
                g[v]+=2
                g[v+1]+=1
                g[v+2]+=1
                for i in range(14,-1,-1):
                   if g[i]==15:
                        for j in range(i,14):
                           g[i]=g[i+1]
                        a[r-1]-=1
                        a[r]-=1
                        
                print("b "+str(c)+" "+str(r))
            elif rt=="c":
               max1=a[0]
               ii=0
               for i in range(len(a)-1):
                    if a[i]>max1:
                        max1=a[i]
                        ii=i
               r=ii+1
               #r=random.randint(1,14)
               x=min(a[r-1],a[r])
               c=x+1
               a[r-1]=x-3
               a[r]=x-3
               v=15-c
               g[v]+=1
               g[v+1]+=1
               g[v+2]+=2
               for i in range(14,-1,-1):
                   if g[i]==15:
                        for j in range(i,14):
                           g[i]=g[i+1]
                        a[r-1]-=1
                        a[r]-=1
                        
               print("c "+str(c)+" "+str(r))
            elif rt=="d":
                max1=a[0]
                ii=0
                for i in range(len(a)-2):
                    if a[i]>max1:
                        max1=a[i]
                        ii=i
                r=ii+1
                #r=random.randint(1,13)
                x=min(a[r-1],a[r],a[r+1])
                c=x+1
                a[r-1]=x-2
                a[r]=x-2
                a[r+1]=x-2
                v=15-c
                g[v]+=1
                g[v+1]+=3
                for i in range(14,-1,-1):
                   if g[i]==15:
                        for j in range(i,14):
                           g[i]=g[i+1]
                        a[r-1]-=1
                        a[r]-=1
                        a[r+1]-=1

                print("d "+str(c)+" "+str(r))
        elif fig==3:
            rt=random.choice("abcd")
            if rt=="a":
                 max1=a[0]
                 ii=0
                 for i in range(len(a)-2):
                    if a[i]>max1:
                        max1=a[i]
                        ii=i
                 r=ii+1
                 #r=random.randint(1,13)
                 x=min(a[r-1],a[r],a[r+1])
                 c=x+1
                 a[r-1]=x-1
                 a[r]=x-1
                 a[r+1]=x-2

                 v=15-c
                 g[v]+=3
                 g[v+1]+=1
                 for i in range(14,-1,-1):
                   if g[i]==15:
                        for j in range(i,14):
                           g[i]=g[i+1]
                        a[r-1]-=1
                        a[r]-=1
                        a[r+1]-=1
                 print("a "+str(c)+" "+str(r))
            elif rt=="b":
                max1=a[0]
                ii=0
                for i in range(len(a)-1):
                    if a[i]>max1:
                        max1=a[i]
                        ii=i
                r=ii+1
                #r=random.randint(1,14)
                x=min(a[r-1],a[r])
                c=x+1
                a[r-1]=x-3
                a[r]=x-1
                v=15-c
                g[v]+=2
                g[v+1]+=1
                g[v+2]+=1
                for i in range(14,-1,-1):
                   if g[i]==15:
                        for j in range(i,14):
                           g[i]=g[i+1]
                        a[r-1]-=1
                        a[r]-=1
                print("b "+str(c)+" "+str(r))
            elif rt=="c":
                 max1=a[0]
                 ii=0
                 for i in range(len(a)-2):
                    if a[i]>max1:
                        max1=a[i]
                        ii=i
                 r=ii+1
                 #r=random.randint(1,13)
                 x=min(a[r-1],a[r],a[r+1])
                 c=x+1
                 a[r-1]=x-2
                 a[r]=x-2
                 a[r+1]=x-2
                 v=15-c
                 g[v]+=1
                 g[v+1]+=3
                 for i in range(14,-1,-1):
                   if g[i]==15:
                        for j in range(i,14):
                           g[i]=g[i+1]
                        a[r-1]-=1
                        a[r]-=1
                        a[r+1]-=1
                 print("c "+str(c)+" "+str(r))
            elif rt=="d":
                 max1=a[0]
                 ii=0
                 for i in range(len(a)-1):
                    if a[i]>max1:
                        max1=a[i]
                        ii=i
                 r=ii+1
                # r=random.randint(1,14)
                 x=min(a[r-1],a[r])
                 c=x+1
                 
                 a[r-1]=x-3
                 a[r]=x-3
                 v=15-c
                 g[v]+=1
                 g[v+1]+=1
                 g[v+1]+=2
                 
                 for i in range(14,-1,-1):
                   if g[i]==15:
                        for j in range(i,14):
                           g[i]=g[i+1]
                        a[r-1]-=1
                        a[r]-=1
                        
                 print("d "+str(c)+" "+str(r))
        elif fig==4:
                max1=a[0]
                ii=0
                for i in range(len(a)-1):
                    if a[i]>max1:
                        max1=a[i]
                        ii=i
                r=ii+1
                #r=random.randint(1,14)
                x=min(a[r-1],a[r])
                c=x+1
                a[r-1]=x-2
                a[r]=x-2
                v=15-c
                g[v]+=2
                g[v+1]+=2
                for i in range(14,-1,-1):
                   if g[i]==15:
                        for j in range(i,14):
                           g[i]=g[i+1]
                        a[r-1]-=1
                        a[r]-=1
                               
                print("a "+str(c)+" "+str(r))
        elif fig==5:
            rt=random.choice("ab")
            if rt=="a":
                max1=a[0]
                ii=0
                for i in range(len(a)-2):
                    if a[i]>max1:
                        max1=a[i]
                        ii=i
                r=ii+1
                #r=random.randint(1,13)
                x=min(a[r-1],a[r],a[r+1])
                c=x+1
                a[r-1]=x-1
                a[r]=x-2
                a[r+1]=x-2
                v=15-c
                g[v]+=2
                g[v+1]+=2
                for i in range(14,-1,-1):
                   if g[i]==15:
                        for j in range(i,14):
                           g[i]=g[i+1]
                        a[r-1]-=1
                        a[r]-=1
                        a[r+1]-=1
                print("a "+str(c)+" "+str(r))
            elif rt=="b":
                max1=a[0]
                ii=0
                for i in range(len(a)-1):
                    if a[i]>max1:
                        max1=a[i]
                        ii=i
                r=ii+1
                #r=random.randint(1,14)
                x=min(a[r-1],a[r])
                c=x+1
                a[r-1]=x-3
                a[r]=x-2
                v=15-c
                g[v]+=1
                g[v+1]+=2
                g[v+1]+=1
                for i in range(14,-1,-1):
                   if g[i]==15:
                        for j in range(i,14):
                           g[i]=g[i+1]
                        a[r-1]-=1
                        a[r]-=1
                        
                print("b "+str(c)+" "+str(r))

        elif fig==6:
            rt=random.choice("abcd")
            if rt=="a":
                max1=a[0]
                ii=0
                for i in range(len(a)-2):
                    if a[i]>max1:
                        max1=a[i]
                        ii=i
                r=ii+1
                #r=random.randint(1,13)
                
                x=min(a[r-1],a[r],a[r+1])
                c=x+1
                a[r-1]=x-1
                a[r]=x-2
                a[r+1]=x-1
                v=15-c
                g[v]+=3
                g[v+1]+=1
                for i in range(14,-1,-1):
                   if g[i]==15:
                        for j in range(i,14):
                           g[i]=g[i+1]
                        a[r-1]-=1
                        a[r]-=1
                        a[r+1]-=1
                print("a "+str(c)+" "+str(r))

            elif rt=="b":
                max1=a[0]
                ii=0
                for i in range(len(a)-1):
                    if a[i]>max1:
                        max1=a[i]
                        ii=i
                r=ii+1
                #r=random.randint(1,14)
                x=min(a[r-1],a[r])
                c=x+1
                a[r-1]=x-3
                a[r]=x-2
                v=15-c
                g[v]+=1
                g[v+1]+=2
                g[v+2]+=1
                for i in range(14,-1,-1):
                   if g[i]==15:
                        for j in range(i,14):
                           g[i]=g[i+1]
                        a[r-1]-=1
                        a[r]-=1
                        
                print("b "+str(c)+" "+str(r))

            elif rt=="c":
                max1=a[0]
                ii=0
                for i in range(len(a)-2):
                    if a[i]>max1:
                        max1=a[i]
                        ii=i
                r=ii+1
                #r=random.randint(1,13)
                
                x=min(a[r-1],a[r],a[r+1])
                c=x+1
                a[r-1]=x-2
                a[r]=x-2
                a[r+1]=x-2
                v=15-c
                g[v]+=1
                g[v+1]+=3
                for i in range(14,-1,-1):
                   if g[i]==15:
                        for j in range(i,14):
                           g[i]=g[i+1]
                        a[r-1]-=1
                        a[r]-=1
                        a[r+1]-=1
                print("c "+str(c)+" "+str(r))

            elif rt=="d":
                max1=a[0]
                ii=0
                for i in range(len(a)-1):
                    if a[i]>max1:
                        max1=a[i]
                        ii=i
                
                #r=random.randint(1,14)
                x=min(a[r-1],a[r])
                c=x+1
                
                a[r-1]=x-2
                a[r]=x-3
                v=15-c
                g[v]+=1
                g[v+1]+=2
                g[v+2]+=1
                for i in range(14,-1,-1):
                   if g[i]==15:
                        for j in range(i,14):
                           g[i]=g[i+1]
                        a[r-1]-=1
                        a[r]-=1
                    
                print("d "+str(c)+" "+str(r))
        elif fig==7:
            rt=random.choice("ab")
            if rt=="a":
                max1=a[0]
                ii=0
                for i in range(len(a)-2):
                    if a[i]>max1:
                        max1=a[i]
                        ii=i
                r=ii+1
                #r=random.randint(1,13)
                x=min(a[r-1],a[r],a[r+1])
                c=x+1
                a[r-1]=x-2
                a[r]=x-2
                a[r+1]=x-1
                v=15-c
                g[v]+=2
                g[v+1]+=2
                for i in range(14,-1,-1):
                   if g[i]==15:
                        for j in range(i,14):
                           g[i]=g[i+1]
                        a[r-1]-=1
                        a[r]-=1
                        
                print("a "+str(c)+" "+str(r))
            elif rt=="b":
                max1=a[0]
                ii=0
                for i in range(len(a)-1):
                    if a[i]>max1:
                        max1=a[i]
                        ii=i
                r=ii+1
                #r=random.randint(1,14)
                x=min(a[r-1],a[r])
                c=x+1
                a[r-1]=x-2
                a[r]=x-3
                v=15-c
                g[v]+=1
                g[v+1]+=2
                g[v+2]+=1
                for i in range(14,-1,-1):
                   if g[i]==15:
                        for j in range(i,14):
                           g[i]=g[i+1]
                        a[r-1]-=1
                        a[r]-=1
                    
                print("b "+str(c)+" "+str(r))               
                    
