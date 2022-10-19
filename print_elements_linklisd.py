"""
Berilgan linked list sonlarini ekranga chiqaring.
Misol: 1->2->3
Kutilgan natija:
1
2
3
"""

class Node:
    def __init__(self, val: int):
        self.val = val
        self.next = None

def print_elements(head: Node) -> None:
    """
    Kodni bu yerda yozing.
    """
    curr = head
    while curr is not None:
        print(curr.val)
        curr = curr.next