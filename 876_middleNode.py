# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        i = j = head
        while j and j.next:
            i = i.next
            j = j.next.next
        return i
