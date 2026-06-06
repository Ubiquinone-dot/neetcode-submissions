# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        # Oneliner
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root

        # def invert(leaf):
        #     if leaf is None:
        #         return leaf

        #     # Swap both leaves
        #     tmp = leaf.left
        #     leaf.left=leaf.right
        #     leaf.right=tmp

        #     # Then swap children of the leaf
        #     leaf.left = invert(leaf.left)
        #     leaf.right = invert(leaf.right)
            
        #     return leaf
        
        # return invert(root)