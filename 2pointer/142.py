# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: ListNode):
        if not head:
            return None
        slow = fast = head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
            if slow == fast:
                break
        if not fast or not fast.next:
            return None
        slow = head
        while slow != fast:
            slow, fast = slow.next, fast.next
        return slow
