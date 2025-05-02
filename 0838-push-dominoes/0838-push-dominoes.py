class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        # Algorithms: Two Pointers with Greedy
        # Time & Space Complexity O(n)

        res = []
        r, dots = False, 0

        for d in dominoes:
            if d == ".":
                dots += 1
            elif d == "R":
                if r:
                    res.append("R" * (dots + 1))
                elif dots > 0:
                    res.append("." * dots)
                
                r, dots = True, 0

            else:
                if r:
                    res.append("R")
                    if dots > 0:
                        res.append("R" * (dots // 2))
                        if dots % 2 == 1:
                            res.append(".")
                        res.append("L" * (dots // 2))
                    res.append("L")
                    r, dots = False, 0
                else:
                    res.append("L" * (dots + 1))
                    dots = 0
        if r:
            res.append("R" * (dots + 1))
        else:
            res.append("." * dots)
        return "".join(res)