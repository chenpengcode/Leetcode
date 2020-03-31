# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        slow, fast = head, head.next
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next

        mid, slow.next = slow.next, None

        left = self.sortList(head)
        right = self.sortList(mid)

        h = res = ListNode(-1)
        while left and right:
            if left.val <= right.val:
                h.next, left = left, left.next
            else:
                h.next, right = right, right.next
            h = h.next

        h.next = left if left else right
        return res.next

    def sort_list(self, head: ListNode) -> ListNode:
        len_list = 0
        len_to_merge = 1
        h = head

        while h:
            h = h.next
            len_list += 1

        res = ListNode(-1)
        res.next = head

        while len_to_merge < len_list:
            pre = res
            h = res.next
            while h:
                h1 = h
                len_first = len_to_merge
                while h and len_first:
                    h = h.next
                    len_first -= 1

                if len_first:
                    break

                h2 = h
                len_second = len_to_merge
                while h and len_second:
                    h = h.next
                    len_second -= 1

                len_lst_1 = len_to_merge - len_first
                len_lst_2 = len_to_merge - len_second
                while len_lst_1 and len_lst_2:
                    if h1.val < h2.val:
                        pre.next = h1
                        h1 = h1.next
                        len_lst_1 -= 1
                    else:
                        pre.next = h2
                        h2 = h2.next
                        len_lst_2 -= 1
                    pre = pre.next
                pre.next = h1 if len_lst_1 else h2
                while len_lst_1 > 0 or len_lst_2 > 0:
                    pre = pre.next
                    len_lst_1 -= 1
                    len_lst_2 -= 1
                pre.next = h
            len_to_merge *= 2
        return res.next
