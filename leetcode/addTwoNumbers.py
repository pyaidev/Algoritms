# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        left = 0
        dummy = cur = ListNode(-1)
        while l1 or l2 or left:
            left, sm = divmod(sum(i and i.val or 0 for i in (l1, l2)) + left, 10)  # divmod() a//b and a % b
            cur.next = cur = ListNode(sm)
            l1 = l1 and l1.next
            l2 = l2 and l2.next
        return dummy.next
