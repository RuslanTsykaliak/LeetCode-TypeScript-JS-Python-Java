class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        # DFS+BT is tempting but not suitable, combinatorial number of ways, can't enumerate

        # BUT WAIT: <= k becomes unusable for ALL strings!!!!

        # so DP is on the menu, current state is
        #   i: next char of target
        #   k: next index

        # we don't care about which string the char comes from, just the count
        BIG = 10**9 + 7

        K = max(len(w) for w in words)
        N = len(target)
        oa = ord("a")

        # for current state i, k we need to know how many copies of target[i] exist at indices k in words
        # so for each char and k we need counts

        counts = [[0] * K for _ in range(26)]
        for w in words:
            for k, c in enumerate(w):
                o = ord(c) - oa
                counts[o][k] += 1

        @cache
        def countWays(i: int, k: int) -> int:
            if i == N:
                return 1
            if k + (N - i) > K:
                return 0

            skip = countWays(i, k + 1)
            freq = counts[ord(target[i]) - oa][k]
            take = freq * countWays(i + 1, k + 1) if freq else 0

            return (skip + take) % BIG

        return countWays(0, 0)

        return countWays(0, 0)

        # fancier: use bottom-up DP
        #     ways(i,k) depends on ways(i, k+1) and ways(i+1, k)
