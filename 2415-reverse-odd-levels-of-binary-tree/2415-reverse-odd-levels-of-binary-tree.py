# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        q, level = deque(), 0
        q.append([root])
        while q:
            temp = q.pop()
            curr_level, next_level = [], []
            for node in temp:
                curr_level.append(node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            if len(next_level) > 0:
                q.append(next_level)
            if level % 2 != 0:
                i = len(curr_level) - 1
                for node in temp:
                    node.val = curr_level[i]
                    i -= 1
            level += 1
        return root
