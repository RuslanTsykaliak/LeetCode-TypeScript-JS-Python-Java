class Solution:
    def smallestUniqueSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        
        # Initial ranks
        rank = sorted(set(nums))
        comp = {v: i for i, v in enumerate(rank)}
        rank = [comp[x] for x in nums]

        sa = list(range(n))
        k = 1
        tmp = [0] * n

        while k < n:
            # One sort suffices (tuple comparison handles both keys)
            sa.sort(key = lambda i: (rank[i], rank[i + k] if i + k < n else -1))

            tmp[sa[0]] = 0
            prev = sa[0]
            for idx in range(1, n):
                cur = sa[idx]
                a1 = rank[prev]
                a2 = rank[prev + k] if prev + k < n else -1
                b1 = rank[cur]
                b2 = rank[cur + k] if cur + k < n else -1
                tmp[cur] = tmp[prev] + (0 if (a1 == b1 and a2 == b2) else 1)
                prev = cur
            
            rank, tmp = tmp, rank
            if rank[sa[-1]] == n - 1:
                break
            k <<= 1
        
        # Kasai LCP
        pos = [0] * n
        for i in range(n):
            pos[sa[i]] = i
        
        lcp = [0] * n
        h = 0
        for i in range(n):
            pi = pos[i]
            if pi == 0:
                h = 0
                continue
            j = sa[pi - 1]
            while i + h < n and j + h < n and nums[i + h] == nums[j + h]:
                h += 1
            lcp[pi] = h
            if h:
                h -= 1
        
        answer = n
        for i in range(n):
            nxt = lcp[i + 1] if i + 1 < n else 0
            need = (lcp[i] if lcp[i] > nxt else nxt) + 1
            if sa[i] + need - 1 < n and need < answer:
                answer = need
                
        return answer