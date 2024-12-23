# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:

        def calculate_swaps(arr):
            n = len(arr)
            sorted_indices = sorted(
                range(n), key=lambda x: arr[x]
            )  # Indices of sorted array
            visited = [False] * n
            swaps = 0

            for i in range(n):
                if visited[i] or sorted_indices[i] == i:
                    continue  # Skip already visited or correctly placed elements

                # Count cycle length
                cycle_length = 0
                j = i
                while not visited[j]:
                    visited[j] = True
                    j = sorted_indices[j]
                    cycle_length += 1

                if cycle_length > 1:
                    swaps += cycle_length - 1

            return swaps

        q = deque()
        temp = []
        q.append((root))
        cnt = 0
        while q:
            node = q.popleft()
            if node.left:
                temp.append(node.left)
            if node.right:
                temp.append(node.right)
            if not q:
                arr = [n.val for n in temp]
                cnt += calculate_swaps(arr)
                q = deque(temp)
                temp = []
        return cnt
