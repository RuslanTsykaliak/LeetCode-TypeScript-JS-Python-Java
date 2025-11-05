class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        sl = SortedList()
        freq = Counter()
        ans = []
        total = 0

        def add(v):
            ans = 0
            sl.add((-freq[v], -v))
            j = sl.bisect_left((-freq[v], -v))
            if j < x:
                ans += freq[v] * v
                if len(sl) > x:
                    ff, vv = sl[x]
                    ans -= ff * vv
            return ans

        def remove(v):
            ans = 0
            j = sl.bisect_left((-freq[v], -v))
            if j < x:
                ans -= freq[v] * v
                if len(sl) > x:
                    ff, vv = sl[x]
                    ans += ff * vv
            sl.remove((-freq[v], -v))
            return ans

        for i, v in enumerate(nums):
            if freq[v]:
                total += remove(v)
            freq[v] += 1
            total += add(v)
            if i >= k:
                total += remove(nums[i - k])
                freq[nums[i - k]] -= 1
                if freq[nums[i - k]]:
                    total += add(nums[i - k])
            if i >= k - 1:
                ans.append(total)
        return ans
