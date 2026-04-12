class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0

        def dfs(node, maxVal):
            nonlocal count
            if not node:
                return

            # Check if the current node is a good node
            if node.val >= maxVal:
                count += 1

            # Update the maximum value seen so far
            maxVal = max(maxVal, node.val)

            # Traverse left and right subtrees
            dfs(node.left, maxVal)
            dfs(node.right, maxVal)

        dfs(root, float("-inf"))
        return count