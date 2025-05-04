class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        count_map = defaultdict(int)
        for a, b in dominoes:
             # Normalize (a, b) to always have (min, max)
             key = (min(a, b), max(a, b))
             count_map[key] += 1
        
        res = 0
        for c in count_map.values():
            if c > 1:
                res += c * (c - 1) // 2
        return res