#smallest number in the next array elements
l=[5,4,1,10,3]
op=[1,1,-1,3,-1]
d=[]
for i in range(len(l)):
    v=l[i]
    for j in range(i+1,len(l)):
        v=min(v,l[j])
    if v==l[i]:
        d.append(-1)
    elif v!=l[i] and i<len(l):
        d.append(v)
print(d)