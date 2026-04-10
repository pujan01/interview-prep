# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        queue = collections.deque()
        
        if root: queue.append(root)

        while queue:
            qLen = len(queue)
            level = []
            for _ in range(qLen):
                num = queue.popleft()
                level.append(num.val)
                if num.left: queue.append(num.left)
                if num.right: queue.append(num.right)

            res.append(level)

        return res


        


            
            