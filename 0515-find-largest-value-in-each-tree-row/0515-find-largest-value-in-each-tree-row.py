# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:

        def dfs(v, d):
            if v != None:
                if len(ans) == d:
                    ans.append(v.val)
                else:
                    ans[d] = max(ans[d], v.val)
                dfs(v.left, d + 1)
                dfs(v.right, d + 1)

        ans = []
        dfs(root, 0)
        return ans
