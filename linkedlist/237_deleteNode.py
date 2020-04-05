# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next


if __name__ == '__main__':
    test = Solution()
    head = ListNode(4)
    node1 = ListNode(5)
    node2 = ListNode(1)
    node3 = ListNode(2)
    head.next = node1
    node1.next = node2
    node2.next = node3
    test.deleteNode(node1)
    print(head.val)
    print(head.next.val)
