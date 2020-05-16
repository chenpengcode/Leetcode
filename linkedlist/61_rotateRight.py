# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or not head.next:
            return head
        p = head
        n = 0
        while p:
            n += 1
            p = p.next
        k %= n
        # k移动n的整数倍，相当于没有移动
        if k == 0:
            return head
        pre = ListNode(0)
        pre.next = head
        slow = fast = head
        for i in range(k - 1):
            fast = fast.next
        while fast and fast.next:
            pre = pre.next
            slow = slow.next
            fast = fast.next
        fast.next = head
        pre.next = None
        return slow
