from operator import index


l=[1,2,3,1,2,3,8]
count=0
b=1
for i in range(len(l)):
    if i%4==0:
        pass
    else:
        for j in range(i+1,len(l)-1):
            if (l[i]+l[j])%4==0:
                l.append(l[i]+l[j])
                l.pop(l.index(l[i]))
                l.pop(l.index(l[j]))
                count+=1
for i in l:
    if i%4!=0:
        b=-1
        break
if b==1:
    print(count)
elif b==-1:
    print(-1)
