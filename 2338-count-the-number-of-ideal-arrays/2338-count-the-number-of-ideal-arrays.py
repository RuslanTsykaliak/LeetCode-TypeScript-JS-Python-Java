class Solution:
    MOD = 10**9 + 7
    def idealArrays(self, n: int, maxValue: int) -> int:
        # Algorithms: Sieve of Eratosthenes + Combinatorics + Prime-power factorization

        # 1) Sieve for smallest prime divisor
        mind = [0] * (maxValue + 1)
        for p in range(2, maxValue + 1):
            if mind[p] == 0:
                for i in range(p, maxValue + 1, p):
                    if mind[i] == 0:
                        mind[i] = p
        
        # 2) Precompute binomial coeffcients C(n + i - 1, i)
        maxPow = int(log2(maxValue)) + 1
        C = [1] * (maxPow + 1)
        for i in range(1, maxPow + 1):
            C[i] = comb(n + i - 1, i) % self.MOD
        
        # 3) Factor each i and multiply choices per prime exponent
        ans = 0
        for i in range(1, maxValue + 1):
            x, prod = i, 1
            while x > 1:
                p, exp = mind[x], 0
                while x % p == 0:
                    x //= p
                    exp += 1
                prod = prod * C[exp] % self.MOD
            ans = (ans + prod) % self.MOD
        return ans

