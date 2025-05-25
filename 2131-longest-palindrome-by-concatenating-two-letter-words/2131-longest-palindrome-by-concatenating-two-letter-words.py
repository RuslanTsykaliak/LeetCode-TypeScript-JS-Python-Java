class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        map = {}
        occur = False
        count = 0
        for word in words:
            map[word] = (map[word]+1) if word in map else 1
        for key in map:
            rev = key[1] + key[0]
            if key!=rev and rev in map:
                count+= min(map[key],map[rev])*2
                map[key] = 0
            elif key == rev:
                if map[key]%2!=0:
                    occur = True
                    map[key] -= 1
                count += map[key] + (-1 if map[key]%2!=0 else 0)
                map[key] = 0
        return count*2 + (2 if occur else 0)
