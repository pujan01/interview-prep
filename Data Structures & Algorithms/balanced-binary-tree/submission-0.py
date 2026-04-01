# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:
                return True, 0 
            left, lh = dfs(node.left)
            right, rh = dfs(node.right)
            if left and right and abs(lh - rh) <= 1:
                return True, max(lh, rh) + 1
            else:
                return False, max(lh, rh) + 1
        
        ans, h = dfs(root)
        print(ans,h)
        return ans