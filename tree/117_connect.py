# Definition for a Node.
import collections


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
            return root

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
        while leftmost:
            head = tail = Node()
            cur = leftmost

            while cur:
                if cur.left:
                    tail.next = cur.left
                    tail = tail.next
                if cur.right:
                    tail.next = cur.right
                    tail = tail.next
                cur = cur.next
            leftmost = head.next
        return root

