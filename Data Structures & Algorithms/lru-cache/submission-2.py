class Node:
    def __init__(self, key, value= None, prev = None, next = None):
        self.key = key
        self.value = value
        self.prev = prev 
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.oldest = Node(0,0)
        self.latest = Node(0, 0,self.oldest)
        self.oldest.next = self.latest

    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    def insert(self, node):
        prev = self.latest.prev
        prev.next = self.latest.prev = node 
        node.prev = prev
        node.next = self.latest

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])
        
        if len(self.cache) > self.capacity:
            del self.cache[self.oldest.next.key]
            self.remove(self.oldest.next)
