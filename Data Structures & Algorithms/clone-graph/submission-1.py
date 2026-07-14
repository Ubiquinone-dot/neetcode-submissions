"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:

    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        hm = {}
        def dfs(root):
            if root in hm:
                return hm[root]
            copy = Node(root.val)  # do NOT yet create the neighbour graph for this node
            hm[root] = copy
            for n in root.neighbors:
                copy.neighbors.append(dfs(n))  # update in-place with new vals
            return copy
        
        return dfs(node) if node else None

