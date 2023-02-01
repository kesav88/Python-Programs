class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

    
class SLL:
    def __init__(self):
        self.head=None

    
    def display(self):
        if self.head is None:
            print("empty")
        else:
            temp=self.head
            while temp:
                print(temp.data)
                temp=temp.next


L=SLL()
n1=Node(10)
L.head=n1
n2=Node(20)
n1.next=n2
n3=Node(30)
n2.next=n3
L.display()