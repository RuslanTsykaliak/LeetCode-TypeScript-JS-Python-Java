# Beats 100% Single Pass: Return False on the First "ba"

# Intuition
Every 'a' comes before every 'b' only if no 'b' is ever directly followed by an 'a'. So we only need to look for the substring "ba".

# Approach
Loop through the string from index 1. Compare each character with the one before it. If we find 'b' then 'a', return `false`. If the loop finishes, return `true`.

# Complexity
- Time complexity: $$O(n)$$

- Space complexity: $$O(1)$$

# Video
https://youtu.be/9WSrjuDB2YU

# Code
```python3 []
class Solution:
    def checkString(self, s: str) -> bool:
        # Input: string s containing 'a's and 'b's
        # Output: true or false
        # Process: if any 'a' appears after 'b'

        for a in range(1, len(s)):
            if s[a - 1] == "b" and s[a] == "a":
                return False
        return True
```
```typescript []
function checkString(s: string): boolean {
    for (let a = 1; a < s.length; a++) {
        if (s[a - 1] == "b" && s[a] == "a") {
            return false;
        }
    }
    return true;
};
```
```java []
class Solution {
    public boolean checkString(String s) {
        for (int a = 1; a < s.length(); a++) {
            if (s.charAt(a - 1) == 'b' && s.charAt(a) == 'a') {
                return false;
            }
        }
        return true;
    }
}
```