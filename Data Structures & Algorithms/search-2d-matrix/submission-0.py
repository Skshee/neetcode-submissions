class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        left = 0
        right = m * n -1

        while left <= right:
            mid = (left + right) // 2

            midRow = mid // n
            midCol = mid % n

            if matrix[midRow][midCol] == target:
                return True
            elif matrix[midRow][midCol] > target:
                right = mid - 1
            else:
                left = mid + 1
        return False
        