class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        queue = deque()
        queue.append(root)

        res = []

        while queue:
            levelNodes = len(queue)
            currNodes = []

            for _ in range(levelNodes):
                node = queue.popleft()
                currNodes.append(node.val)

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            res.append(currNodes)

        return res