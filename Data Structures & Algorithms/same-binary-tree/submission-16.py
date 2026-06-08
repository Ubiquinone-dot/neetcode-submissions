# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        self.same=True

        def dfs(leaf1, leaf2):
            print(0, leaf1, leaf2)
            if leaf1 is None and leaf2 is None:
                return True
            elif (leaf1 is None and leaf2 is not None) or (
                leaf1 is not None and leaf2 is None):
                return False
            
            l = dfs(leaf1.left, leaf2.left)
            r = dfs(leaf1.right, leaf2.right)
            self.same = l and r and self.same

            return leaf1.val == leaf2.val and self.same

        if p and not q:
            return False
        if q and not p:
            return False

        self.same =  dfs(p, q)
        
        return self.same