from collections import Counter
l=[3,2,3,4,5,6,7,7,8,9]
d=Counter(l)
for i in l:
    if d.get(i)>len(l)/2:
        print(i)
        break

    
   
    
    
 
 
