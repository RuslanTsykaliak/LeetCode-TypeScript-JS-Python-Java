class Solution:
    def countAndSay(self, n: int) -> str:
        # Start from the base term
        s = "1"
        # Iteratively build up to the nth term
        for _ in range(n - 1):
            s = self._next_term(s)
        return s
    
    def _next_term(self, s: str) -> str:
        # Run-length encode the string s
        # Use a list buffer for O(m) concatenation
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
        # Append the final run
        buf.append(str(count))
        buf.append(prev)
        return "".join(buf)