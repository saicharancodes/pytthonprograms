n=int(input())
l=[]
for i in range(n):
    l.append(int(input()))
s=list(set(l))
print(len(l)-len(s))
2