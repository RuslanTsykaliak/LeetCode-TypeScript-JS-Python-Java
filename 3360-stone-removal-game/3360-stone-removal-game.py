class Solution:
    def canAliceWin(self, n: int) -> bool:
        # just playing around :)
        if n < 10:
            return False
        if n > 9 and n < 19:
            return True
        if n > 18 and n < 27:
            return False
        if n > 26 and n < 34:
            return True
        if n > 33 and n < 40:
            return False
        if n > 39 and n < 45:
            return True
        if n > 44 and n < 49:
            return False
        if n > 48 and n < 51:
            return True