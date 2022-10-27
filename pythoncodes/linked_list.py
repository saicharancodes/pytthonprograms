
class Example:
  #  def __init__(self,data):
  #      self.data=data
  #      self.ref=None
    def __init__(self):
        self.head=None
    def datalist(self):
       
        if self.head is None:
            print("linked list is empty")
        else:
            n=self.head
            while n is not None:
                print(n.data)
                n=n.ref

ll1=Example()
print(ll1.datalist)