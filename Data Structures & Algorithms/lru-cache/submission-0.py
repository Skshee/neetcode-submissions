class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.nodeMap = {}

        # Dummy nodes
        self.head = Node(-1, -1)  # LRU side
        self.tail = Node(-1, -1)  # MRU side

        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.nodeMap:
            return -1

        node = self.nodeMap[key]

        # Move node to MRU position
        self.remove(node)
        self.add(node)

        return node.val

    def put(self, key: int, value: int) -> None:
        # If key already exists, remove old node
        if key in self.nodeMap:
            self.remove(self.nodeMap[key])

        node = Node(key, value)
        self.add(node)

        # Remove LRU node if capacity exceeded
        if len(self.nodeMap) > self.capacity:
            lru = self.head.next
            self.remove(lru)

    def add(self, node):
        """
        Add node right before tail (MRU position)
        """
        self.nodeMap[node.key] = node

        prevNode = self.tail.prev

        prevNode.next = node
        node.prev = prevNode

        node.next = self.tail
        self.tail.prev = node

    def remove(self, node):
        """
        Remove node from DLL and hashmap
        """
        del self.nodeMap[node.key]

        prevNode = node.prev
        nextNode = node.next

        prevNode.next = nextNode
        nextNode.prev = prevNode