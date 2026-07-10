class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = {}
        if amount == 0:
            return 1
        for ci in range(len(coins)-1,-1,-1):
            for k in range(1, amount+1):
                dp[(ci, k)] = dp[(ci+1, k)] if ci != len(coins)-1 else 0
                if k >= coins[ci]:
                    if (ci, k-coins[ci]) in dp:
                        dp[(ci, k)] += dp[(ci, k - coins[ci])]
                    else:
                        dp[(ci, k)] += 1
        return dp[(0,amount)]

        # res = 0

        # def dfs(cursum, i):
        #     nonlocal res
        #     if cursum > amount:
        #         return
        #     elif cursum == amount:
        #         res+=1
        #         return
        #     if i >= len(coins):
        #         return

        #     dfs(cursum, i+1)  # search next in sequence
        #     dfs(cursum + coins[i], i) # take current in sequence

        #     return

        # dfs(0, 0)

        # return res