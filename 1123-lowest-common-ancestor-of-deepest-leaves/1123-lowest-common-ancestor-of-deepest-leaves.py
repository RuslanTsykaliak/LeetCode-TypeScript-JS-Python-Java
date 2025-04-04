# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Algorithm: Binary Search (most likely). DFS. BFS
        # Input: the root of a binary tree
        # Output: the lowest common ancestor of its deepest leaves: The lowes elements in the binary tree

        # Recursion
        def dfs(root):
            if not root:
                return 0, None
            
            left = dfs(root.left)
            right = dfs(root.right)
            
            if left[0] > right[0]:
                return left[0] + 1, left[1]
            if left[0] < right[0]:
                return right[0] + 1, right[1]
            return left[0] + 1, root
        
        return dfs(root)[1]
        