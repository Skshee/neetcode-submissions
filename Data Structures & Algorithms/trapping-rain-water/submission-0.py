class Solution:
    def trap(self, height: List[int]) -> int:
        # l_wall and r_wall stores current highest left height and right height from current position respectively
        l_wall, r_wall = 0,0
        n = len(height)
        max_right = [0] * n
        max_left = [0] * n

        for i in range(n):
            j = -i - 1
            max_left[i] = l_wall
            max_right[j] = r_wall
            l_wall = max(l_wall, height[i])
            r_wall = max(r_wall, height[j])
        print(max_left)
        print(max_right)

        summ = 0

        for i in range(n):
            minHeight = min(max_left[i], max_right[i])
            if (minHeight - height[i]) > 0:
                summ += minHeight - height[i]
        return summ
