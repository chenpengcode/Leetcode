# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head or not head.next:
            return True

        pre = None
        slow = fast = r = head

        while fast and fast.next:
            r = slow
            slow = slow.next
            fast = fast.next.next
            r.next = pre
            pre = r
        if fast:
            slow = slow.next

        while r:
            if slow.val != r.val:
                return False
            slow = slow.next
            r = r.next
        return True
