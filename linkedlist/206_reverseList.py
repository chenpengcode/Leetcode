# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or head.next:
            return head

        p = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return p

    def reverse_list(self, head: ListNode) -> ListNode:
        pre_node = None
        cur_node = head
        while cur_node:
            tmp = cur_node.next
            cur_node.next = pre_node
            pre_node = cur_node
            cur_node = tmp
        return pre_node
