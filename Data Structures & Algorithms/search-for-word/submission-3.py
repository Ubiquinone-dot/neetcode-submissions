class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        J=len(board[0])
        I=len(board)
        def check_sub(i0, j0, k, seen):
            if i0 == I or j0 == J or i0 < 0 or j0 < 0 or k >= len(word):
                return False
            if (i0, j0) in seen:
                return False
            if board[i0][j0] == word[k]:
                if k == len(word)-1:
                    return True
                seen = seen | {(i0, j0)}
                up = check_sub(i0-1, j0, k+1, seen)
                left = check_sub(i0, j0-1, k+1, seen)
                right = check_sub(i0, j0+1, k+1, seen)
                down = check_sub(i0+1, j0, k+1, seen)
                return up or down or left or right
            return False
        print(board)
        def traverse():
            for i in range(I):
                for j in range(J):
                    if board[i][j] == word[0]:
                        print("Se", i,j)
                        if check_sub(i, j, k=0, seen=set()):
                            return True
            return False
        return traverse()