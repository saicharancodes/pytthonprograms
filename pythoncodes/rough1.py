nums=[1,4,9]
sum=0
while len(nums)!=0:
    num=min(nums)
    sum+=num
    p=nums.index(num)
    if p+1< len(nums):
        nums.remove(nums[p+1])
    if p-1!=-1:
        nums.remove(nums[p-1]) 
    nums.remove(num)    
print(sum)   

