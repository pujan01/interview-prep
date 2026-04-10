# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        queue = []
        if root:
            queue.append(root)

        while queue:
            level = []
            l = []
            for num in queue:
                l.append(num.val)
                level.append(num)
                
            queue = []
            res.append(l)
            for num in level:
                if num.left: queue.append(num.left)
                if num.right: queue.append(num.right)

        return res


        


            
            