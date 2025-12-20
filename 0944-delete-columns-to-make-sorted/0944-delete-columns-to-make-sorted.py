class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        m, n = len(strs[0]), len(strs)
        ans = 0
        for i in range(m):
            for j in range(1, n):
                if strs[j - 1][i] > strs[j][i]:
                    ans += 1
                    break
        return ans
