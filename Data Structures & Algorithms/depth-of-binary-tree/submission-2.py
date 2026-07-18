# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        queue = deque()
        queue.append(root)
        self.depth = 0

        if not root:
            return 0

        while queue:
            length = len(queue)
            self.depth += 1

            for _ in range(length):
                node = queue.popleft()

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return self.depth
        