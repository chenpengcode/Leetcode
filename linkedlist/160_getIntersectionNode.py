# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        ha = headA
        hb = headB

        while ha != hb:
            ha = ha.next if ha else hb
            hb = hb.next if hb else ha

        return ha
