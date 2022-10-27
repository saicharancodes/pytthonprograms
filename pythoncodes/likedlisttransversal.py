class node:
    def __init__ (self,data=None):
        self.data=data
        self.next=None
class linkedlist:
    def __init__(self):
        self.head=node()
    def addelements(self,data):
        newnode=node(data)
        temp=self.head
        while temp.next != None:
            temp=temp.next
        temp.next=newnode
            
    def printelements(self):
        temp=self.head
        while temp.next!=None:
            temp=temp.next
            print(temp.data)
        
obj=linkedlist()  
obj.addelements(20)
obj.addelements(222)
obj.addelements(2233)
obj.printelements()
        
        