class node:
    def __init__(self,data=None):
        self.data=data
        self.next=None
class linkedlist:
    def __init__(self):
        self.head=node()
    def appendelements(self,data):
        newnode=node(data)
        temp=self.head
        while temp.next!=None:
            temp=temp.next
        temp.next=newnode
    def length(self):
        length=0
        temp=self.head
        while temp.next!=None:
            length+=1
            temp=temp.next
        return length
    def printindex(self,index):
        s=0
        temp=self.head
        while temp.next!=None:
            if s==index:
                print(temp.data)
            s+=1
            temp=temp.next

obj=linkedlist()
l=[1,2,3,4,44,55,5]
for i in l:
    obj.appendelements(i)
print(obj.length())
obj.printindex(5)
