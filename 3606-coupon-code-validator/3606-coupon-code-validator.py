class Solution:
    def validateCoupons(
        self, code: List[str], businessLine: List[str], isActive: List[bool]
    ) -> List[str]:
        mp = {"electronics": 0, "grocery": 1, "pharmacy": 2, "restaurant": 3}
        heap = []
        for c, b, a in zip(code, businessLine, isActive):
            if c:
                x = c.replace("_", "")
                if a and (x.isalnum() or c == "_") and b in mp:
                    heappush(heap, (mp[b], c))

        return [heappop(heap)[1] for _ in range(len(heap))]
