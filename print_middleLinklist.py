"""
Berilgan linked list o'rtasidagi elementni ekranga chiqaring.
Misol: 1->2->3
Kutilgan natija: 2

Yana bir misol: 1->2
Kutilgan natija: 2
"""

class Node:
    def __init__(self, val: int):
        self.val = val
        self.next = None

def print_middle(head: Node) -> None:
    """
    Kodni bu yerda yozing.
    """
    fast = slow = head
    
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    print(slow.val)