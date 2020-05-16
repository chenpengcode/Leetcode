# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def swap(self, head, tail):
        prev = tail.next
        head.next = prev
        tail.next = head
        return tail, head

    def swapPairs_iter(self, head: ListNode) -> ListNode:
        hair = ListNode(0)
        hair.next = head
        pre = hair
        while head and head.next:
            tail = head.next
            nex = tail.next
            head, tail = self.swap(head, tail)
            pre.next = head
            tail.next = nex
            head = nex
            pre = tail
        return hair.next

    def swap_pairs_iter(self, head: ListNode) -> ListNode:
        hair = ListNode(-1)
        hair.next = head
        pre = hair
        while head and head.next:
            first = head
            second = first.next

            pre.next = second
            first.next = second.next
            second.next = first

            pre = first
            head = pre.next
        return hair.next

    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or head.next:
            return head

        first = head
        second = head.next
        first.next = self.swapPairs(second.next)
        second.next = first

        return second
