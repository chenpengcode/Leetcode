# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return
        vec = list()

        node = head
        while node:
            vec.append(node)
            node = node.next

        i, j = 0, len(vec) - 1

        while i < j:
            vec[i].next = vec[j]
            i += 1
            vec[j].next = vec[i]
            j -= 1
        vec[i].next = None

    def reorderList_2(self, head: ListNode) -> None:
        def find_mid(head: ListNode):
            slow = fast = head
            while fast.next and fast.next.next:
                slow = slow.next
                fast = fast.next.next
            return slow

        def reverse(head: ListNode):
            pre = None
            cur = head
            while cur:
                tmp = cur.next
                cur.next = pre
                pre = cur
                cur = tmp
            return pre

        def merge(l1: ListNode, l2: ListNode):
            while l1 and l2:
                tmp1 = l1.next
                tmp2 = l2.next

                l1.next = l2
                l1 = tmp1
                l2.next = l1
                l2 = tmp2

        if not head:
            return
        mid = find_mid(head)
        l1, l2 = head, mid.next
        mid.next = None
        l2 = reverse(l2)
        merge(l1, l2)


if __name__ == '__main__':
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5

    solution = Solution()
    print(solution.reorderList_2(node1))
