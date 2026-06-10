class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Double binary search
        N, M = len(matrix[0]), len(matrix)

        # First locate the row
        l, r = 0, M - 1
        while r >= l:
            m = (r + l) // 2 # middle index
            v = matrix[m][0]
            if target < v:
                r = m - 1
            elif target > v:
                l = m + 1
            else:
                return True
        
        # l=M-1 in cases where matrix[0,M-1] is < target (and loop breaks)
        if l == 0:
            return False
        row = matrix[l-1]

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