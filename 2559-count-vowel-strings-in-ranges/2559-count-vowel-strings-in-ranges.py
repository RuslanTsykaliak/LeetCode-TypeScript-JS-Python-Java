class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        n = len(words)
        vowel = {"a", "e", "i", "o", "u"}
        prefix = [0] * (n + 1)

        for i in range(n):
            curr = words[i]
            if curr[0] in vowel and curr[-1] in vowel:
                prefix[i] = prefix[i - 1] + 1
            else:
                prefix[i] = prefix[i - 1] + 0
        print(prefix)

        result = []
        for l, r in queries:
            result.append(prefix[r] - prefix[l - 1])

        return result
