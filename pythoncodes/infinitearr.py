arr=[1,2,3,4,5,6,6,7,7,8,8,11]
t=11
s=0
e=1
while (t>arr[e]):
    temp=e+1
    e=e+(e-s+1)*2
    s=temp
while s<=e:
    m=s+(e-s)/2
    if t>arr[m]:
        s=m+1
    elif t<arr[m]:
        e=m-1
    else:
        print(arr[m])