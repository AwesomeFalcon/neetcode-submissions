class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) - 1
        while l <= r:
            m = (r - l) // 2 + l
            if matrix[m][0] > target:
                r = m - 1
            elif matrix[m][-1] < target:
                l = m + 1
            else:
                break
        n = (l + r) // 2
        l, r = 0, len(matrix[0]) - 1
        while l <= r:
            m = (r - l) // 2 + l
            if matrix[n][m] < target:
                l = m + 1
            elif matrix[n][m] > target:
                r = m - 1
            else:
                return True
        return False