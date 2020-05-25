class DLinkedNode:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.pre = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.cache = dict()
        self.head = DLinkedNode()
        self.tail = DLinkedNode()
        self.head.next = self.tail
        self.tail.pre = self.head

    def get(self, key: int) -> int:
        if key not in self.cache.keys():
            return -1
        node = self.cache.get(key)
        self.move_to_head(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key not in self.cache.keys():
            node = DLinkedNode(key, value)
            self.cache[key] = node
            self.add_to_head(node)
            self.size += 1
            if self.size > self.capacity:
                removed = self.remove_tail()
                self.cache.pop(removed.key)
                self.size -= 1
        else:
            node = self.cache.get(key)
            node.val = value
            self.move_to_head(node)

    def move_to_head(self, node: DLinkedNode):
        self.remove_node(node)
        self.add_to_head(node)

    def add_to_head(self, node: DLinkedNode):
        node.pre = self.head
        node.next = self.head.next
        self.head.next.pre = node
        self.head.next = node

    def remove_tail(self) -> DLinkedNode:
        node = self.tail.pre
        self.remove_node(node)
        return node

    def remove_node(self, node):
        node.pre.next = node.next
        node.next.pre = node.pre

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
