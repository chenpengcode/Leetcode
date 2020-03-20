# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def add_two_number(self, l1: ListNode, l2: ListNode) -> ListNode:
        l3 = ListNode
        while l1.next and l2.next:
            l3.val = l1.val + l2.val