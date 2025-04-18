class Solution:
    def countAndSay(self, n: int) -> str:
        # "abbccc" we want to say what we see 1a 2b 3c.
        # 122333 we see one 1 two 2 tree 3
        
        s = "1"
        for _ in range(n - 1):
            s = self._next_term(s)
        return s

    def _next_term(self, s: str) -> str:
        buf = []
        count = 1
        prev = s[0]
        for c in s[1:]:
            if c == prev:
                count += 1
            else:
                buf.append(str(count))
                buf.append(prev)
                prev = c
                count = 1
        buf.append(str(count))
        buf.append(prev)
        return "".join(buf)