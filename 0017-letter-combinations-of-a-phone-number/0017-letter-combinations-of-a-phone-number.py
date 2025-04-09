class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = [""]
        if not digits:
            return []
        
        # Manually map all digits to letters
        digits_map = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }
        
        for digit in digits:
            temp = []
            for prefix in res:
                for letter in digits_map[digit]:
                    temp.append(prefix + letter)
            res = temp

        return res

