# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        def get_depth(root, depth):
            if root is None:
                return depth
            elif root.left is None and root.right is None:
                return depth + 1
            elif root.left is None:
                return get_depth(root.right, depth + 1)
            elif root.right is None:
                return get_depth(root.left, depth + 1)
            else:
                return max(get_depth(root.left, depth + 1), get_depth(root.right, depth + 1))
        return get_depth(root, depth=0)

