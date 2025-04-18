class Solution:
    def countAndSay(self, n: int) -> str:
        s = "1"
        for _ in range(n - 1):
            s = self._next_term(s)
        return s

    def _next_term(self, s: str) -> str:
        result = []
        prev_char = s[0]
        count = 1
        for c in s[1:]:
            if c == prev_char:
                count += 1
            else:
                result.append(str(count))
                result.append(prev_char)
                prev_char = c
                count = 1
        # append the final run
        result.append(str(count))
        result.append(prev_char)
        return "".join(result)
