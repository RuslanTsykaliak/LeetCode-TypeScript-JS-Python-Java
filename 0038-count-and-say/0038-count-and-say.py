class Solution:
    h = ["1"]  
    def countAndSay(self, n: int) -> str:
        def u(n):
            if n <= len(Solution.h):  
                return Solution.h[n - 1]  
            else:
                prev = u(n - 1)  
                result = ""
                count = 1

                for i in range(1, len(prev)):
                    if prev[i] == prev[i - 1]:  
                        count += 1
                    else:
                        result += f"{count}{prev[i - 1]}"  
                        count = 1  

                result += f"{count}{prev[-1]}"
                Solution.h.append(result)  
                return result
        return u(n)