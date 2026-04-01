from collections import defaultdict
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head: return None
        oldToCopy = {None: None}
        copyNode = newHead = Node(head.val)
        oldToCopy[head] = newHead
        node = head.next
        while node:
            newNode = Node(node.val)
            oldToCopy[node] = newNode
            node = node.next
        
        copyNode = newHead
        node = head
        while node:
            copyNode.next = oldToCopy.get(node.next)
            copyNode.random = oldToCopy.get(node.random)
            copyNode = copyNode.next
            node = node.next
        
        return newHead
