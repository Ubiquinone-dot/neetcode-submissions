class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Double binary search
        N, M = len(matrix[0]), len(matrix)

        # First locate the row
        l, r = 0, M - 1
        while r >= l:
            m = (r + l) // 2 # middle index
            v = matrix[m][0]
            print(l, r, m)
            if target < v:
                r = m - 1
            elif target > v:
                l = m + 1
            else:
                return True
        row = matrix[max(l-1, 0)]

        # Then, locate the value within the row
        l, r = 0, N - 1
        while r >= l:
            m = (r + l) // 2
            v = row[m]
            if target < v:
                r = m - 1
            elif target > v:
                l = m + 1
            else:
                return True
        return False