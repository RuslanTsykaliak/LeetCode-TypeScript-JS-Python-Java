class Solution:
    def checkString(self, s: str) -> bool:
        # Input: string consistend of a and b
        # Output: True or False
        # Process: Check if the s string has any a after b

        for a in range(1, len(s)):
            if s[a - 1] == "b" and s[a] == "a":
                return False
        return True