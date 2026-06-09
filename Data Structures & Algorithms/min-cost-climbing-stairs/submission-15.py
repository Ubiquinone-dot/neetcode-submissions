class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        # list [6,5,4,3,2,1] for the cost to solve the problem from step index i
        mincost2 = cost[-1]
        mincost1 = cost[-2]

        mincost = [0 for _ in cost]
        for i in reversed(range(len(mincost)-2)):
            # Update cost vars of previous options
            tmp = mincost1
            mincost1 = min(mincost1, mincost2) + cost[i]
            mincost2 = tmp

        return min(mincost1, mincost2)
