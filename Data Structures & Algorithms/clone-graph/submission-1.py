"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        q = deque([node])
        newNode = Node(node.val)
        maps = {node:newNode}
        while q:
            node = q.popleft()
            for nei in node.neighbors:
                if nei not in maps:
                    q.append(nei)
                    maps[nei] = Node(nei.val)
                maps[node].neighbors.append(maps[nei])

        return newNode

