class SinglyNode:
    
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
    
    def __str__(self):
        return str(self.value)
    
Head = SinglyNode(1)
A = SinglyNode(3)
B = SinglyNode(4)
C = SinglyNode(7)

Head.next = A
A.next = B
B.next = C

# Fibonnaci
def F(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return F(n - 1) + F(n - 2)

def reverseList(node):
    if not node:
        return
    
    reverseList(node.next)
    print(node)

reverseList(Head)