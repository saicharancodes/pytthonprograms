'''https://leetcode.com/problems/peak-index-in-a-mountain-//array/ '''
#852
arr=[1,2,4,3,1]
s=0
e=len(arr)-1
while s<e:
    mid=int(s+(e-s)/2)
    if (arr[mid]>arr[mid+1]):
        e=mid
    else:
        s=mid+1
print(s)
