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
        
        maps = {}
        def dfs(node):
            if node not in maps:
                newNode = Node(node.val)
                maps[node] = newNode
                for n in node.neighbors:
                    newNode.neighbors.append(dfs(n))
            return maps[node]
        return dfs(node)
