# Definition for a binary tree node.
import collections


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec_bfs:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        ans = []
        q = collections.deque()
        q.append(root)
        while q:
            node = q.popleft()
            if node:
                ans.append(str(node.val))
                q.append(node.left)
                q.append(node.right)
            else:
                ans.append("None")
        return ",".join(ans)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        nodes_val = data.split(',')
        root_val = nodes_val[0]
        if root_val == "None":
            return None
        root = TreeNode(int(root_val))
        q = collections.deque([root])
        index = 0
        while q:
            node = q.popleft()
            index += 1
            if nodes_val[index] != "None":
                node.left = TreeNode(int(nodes_val[index]))
                q.append(node.left)
            index += 1
            if nodes_val[index] != "None":
                node.right = TreeNode(int(nodes_val[index]))
                q.append(node.right)
        return root


class Codec_dfs:

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
