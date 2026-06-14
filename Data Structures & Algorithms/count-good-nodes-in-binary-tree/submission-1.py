# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return []

        def dfs(node, currMax):
            if not node:
                return 0

            if node.val >= currMax:
                good = 1
                currMax = node.val
            else:
                good = 0

            left = dfs(node.left, currMax)
            right = dfs(node.right, currMax)
            return good + left + right

        return dfs(root, float('-inf'))

            
        