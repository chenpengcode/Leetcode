# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        pre = ListNode(0, head)
        left, right = pre, head
        for _ in range(n):
            right = right.next

        while right:
            left = left.next
            right = right.next
        left.next = left.next.next
        return pre.next
