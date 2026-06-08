# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 0
        
        self.res = 0

        def dfs(curr):
            if not curr:
                return 0

            l = dfs(curr.left)
            r = dfs(curr.right)

            dia = l + r
            self.res = max(self.res, dia)
            return max(l, r) + 1

        dfs(root)
        
        return self.res