# Definition for a binary tree node.
import collections


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        ans = []
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                ans.append(str(node.val))
                stack.append(node.right)
                stack.append(node.left)
            else:
                ans.append("None")
        print(ans)
        return ",".join(ans)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        nodes = collections.deque(data.split(','))
        return self.build(nodes)

    def build(self, nodes):
        node_val = nodes.popleft()
        if node_val == "None":
            return None
        root = TreeNode(int(node_val))
        root.left = self.build(nodes)
        root.right = self.build(nodes)

        return root


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
if __name__ == '__main__':
    data = [1, 2, 3, None, 4]
    for i in range(len(data)):
        data[i] = str(data[i])

    print(",".join(data))
    t = ",".join(data)
    print(t.split(','))
