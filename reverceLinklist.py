"""
Berilgan linked listni teskari qiling.
Misol: 1->2->3
Kutilgan natija: 3->2->1

Yana bir misol: 1->2
Kutilgan natija: 2->1
"""

class Node:
    def __init__(self, val: int):
        self.val = val
        self.next = None

def reverse(head: Node) -> Node:
    """
    Kodni bu yerda yozing.
    """
    prev = None
    curr = head
    
    while curr is not None:
        next_ = curr.next
        curr.next = prev
        prev = curr
        curr = next_
        
    return  prev