import collections


# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None,
                 next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return

        q = collections.deque()
        q.append(root)

        while q:
            cnt = len(q)
            last = q[0]

            for i in range(cnt):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                if i != 0:
                    last.next = node
                last = node

        return root

    def connect_o1(self, root: 'Node') -> 'Node':
        if not root:
            return root

        leftmost = root
        while leftmost.left:
            head = leftmost

            while head:
                head.left.next = head.right
                if head.next:
                    head.right.next = head.next.left
                head = head.next
            leftmost = leftmost.left

        return root

    def connect_rec(self, root: 'Node') -> 'Node':
        if not root:
            return root
        root.left.next = root.right
        if root.next:
            root.right.next = root.next.left
        self.connect_rec(root.left)
        self.connect_rec(root.right)
        return root
