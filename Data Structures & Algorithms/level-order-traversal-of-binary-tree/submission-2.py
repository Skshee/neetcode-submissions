# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.res = []
        queue = deque()
        queue.append(root)

        if not root:
            return []

        while queue:
            length = len(queue)
            currLevel = []

            for _ in range(length):
                node = queue.popleft()
                currLevel.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            self.res.append(currLevel)
        return self.res
                
                



