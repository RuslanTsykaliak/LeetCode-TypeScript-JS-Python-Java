class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        # # Hash Map
        # # Runtime 53%
        # count_map = defaultdict(int)
        # for a, b in dominoes:
        #      # Normalize (a, b) to always have (min, max)
        #      key = (min(a, b), max(a, b))
        #      count_map[key] += 1
        
        # res = 0
        # for c in count_map.values():
        #     if c > 1:
        #         res += c * (c - 1) // 2
        # return res


        # Hash Map 
        # Beats 37%
        # count = Counter()
        # res = 0
        # for a, b in dominoes:
        #     key = (min(a, b), max(a, b))
        #     res += count[key]
        #     count[key] += 1
        # return res

        # Beats 97 %
        seen = [0] * 100
        res = 0
        for a, b in dominoes:
            val = a * 10 + b if a <= b else b * 10 + a
            res += seen[val]
            seen[val] += 1
        return res

