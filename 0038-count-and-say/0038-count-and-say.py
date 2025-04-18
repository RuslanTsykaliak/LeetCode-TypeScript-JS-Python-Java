class Solution:
    h = ["1"]  # Store sequence as strings

    def countAndSay(self, n: int) -> str:
        def u(n):
            if n <= len(Solution.h):  
                return Solution.h[n - 1]  # Retrieve from memoized list
            else:
                prev = u(n - 1)  # Get previous sequence
                result = ""
                count = 1

                for i in range(1, len(prev)):
                    if prev[i] == prev[i - 1]:  
                        count += 1
                    else:
                        result += f"{count}{prev[i - 1]}"  # Append count and digit
                        count = 1  

                # Append last counted group
                result += f"{count}{prev[-1]}"
                Solution.h.append(result)  # Store computed sequence
                return result
        return u(n)