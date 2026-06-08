# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def dfs_inner(root, subroot):
            if (root and not subroot) or (not root and subroot):
                return False
            if not root and not subroot:
                return True
            if not root:
                return False
            if not subroot:
                return False
            return subroot.val == root.val \
                and dfs_inner(root.left, subroot.left) \
                and dfs_inner(root.right, subroot.right)

        self.match=False

        def dfs_outer(root, subroot):
            if not root or self.match:
                return

            if root.val == subroot.val:
                # Start dfs from this node
                self.match = self.match or dfs_inner(root, subroot)

            # Else continue walking tree
            dfs_outer(root.left, subroot)
            dfs_outer(root.right, subroot)

            return 

        dfs_outer(root, subRoot)

        return self.match