class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        req = set([str(n) for n in range(1, 10)])
        [print(b) for b in board]
        print()

        def is_valid(row):
            vals = [v for v in row if v in req]
            # no duplicates
            if not vals:
                return True
            if len(set(vals)) != len(vals):
                return False
            
            return True

        for row in board:
            if not is_valid(row):
                return False
        
        board_transposed = [
            [board[i][j] for i in range(9)]
            for j in range(9)
        ]
        for row in board_transposed:
            if not is_valid(row):
                return False
        
        # Check grids
        for i in range(3):
            for j in range(3):
                vals=[]
                for k in range(3):
                    minirow = board[(3*i) + k][(3*j):(3*j)+3]
                    vals+=minirow

                if not is_valid(vals):
                    return False

        return True