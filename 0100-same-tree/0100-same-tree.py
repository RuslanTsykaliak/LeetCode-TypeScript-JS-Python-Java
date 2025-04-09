# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # # Algorithm: Recursion

        # # If both trees are null
        # if not p and not q:
        #     return True
        
        # # If one of the trees is empty but the other isn't
        # if not p or not q:
        #     return False
        
        # # Compare the values of the current nodes
        # if p.val != q.val:
        #     return False

        # # Call the method to check the left and right subtrees
        # return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

        # Algorithm: Breath First Search

        queue = deque([(p, q)])

        while queue:
            node1, node2 = queue.popleft()
            
            if not node1 and not node2:
                continue
                
            if not node1 or not node2 or node1.val != node2.val:
                return False
                
            queue.append((node1.left, node2.left))
            queue.append((node1.right, node2.right))

        return True
    
        