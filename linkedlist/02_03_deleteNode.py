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
    node_1 = ListNode(4)
    node_2 = ListNode(5)
    node_3 = ListNode(1)
    node_4 = ListNode(9)
    node_1.next = node_2
    node_2.next = node_3
    node_3.next = node_4
    test = Solution()
    test.deleteNode(node_1)
    print(node_1)
