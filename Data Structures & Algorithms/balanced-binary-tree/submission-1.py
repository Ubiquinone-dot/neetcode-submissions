# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        self.res = True

        def dfs(leaf):
            if leaf is None:
                return 0

            l = dfs(leaf.left)
            r = dfs(leaf.right)

            if abs(l - r) > 1:
                self.res=False
                
            return max(l, r) + 1

        dfs(root)

        return self.res