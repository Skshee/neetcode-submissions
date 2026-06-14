# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.lst = []

        def dfs(node):
            if not node:
                return 

            left = dfs(node.left)
            self.lst.append(node.val)
            right = dfs(node.right)

        dfs(root)
        print(self.lst)

        for i in range(1, len(self.lst)):
            if self.lst[i] <= self.lst[i-1]:
                return False
        return True

        
            
        