class Solution:
    def checkString(self, s: str) -> bool:
        # Input: string s containing 'a's and 'b's
        # Output: true or false
        # Process: if any 'a' appears after 'b'

        for a in range(1, len(s)):
            if s[a - 1] == "b" and s[a] == "a":
                return False
        return True