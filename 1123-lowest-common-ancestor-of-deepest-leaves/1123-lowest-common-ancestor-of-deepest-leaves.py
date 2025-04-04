# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Algorithms: DFS. BFS. Can we try  Binary Search?
        # Input: the root of a binary tree
        # Output: the lowest common ancestor of its deepest leaves: The lowes elements in the binary tree

        # Recursion
        # To-Do add explaining comments
        # def dfs(root):
        #     if not root:
        #         return 0, None
            
        #     left = dfs(root.left)
        #     right = dfs(root.right)
            
        #     if left[0] > right[0]:
        #         return left[0] + 1, left[1]
        #     if left[0] < right[0]:
        #         return right[0] + 1, right[1]
        #     return left[0] + 1, root
        
        # return dfs(root)[1]

        # Algorithm: Depth First Search
        # To-do add explaining comments
        def dfs(node, depth):
            if not node:
                return (None, depth + 1)

            left_node, left_depth = dfs(node.left, depth + 1)
            right_node, right_depth = dfs(node.right, depth + 1)

            if left_depth > right_depth:
                return left_node, left_depth
            elif left_depth < right_depth:
                return right_node, right_depth
            return node, left_depth

        node, _ = dfs(root, 0)
        return node


        