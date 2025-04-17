class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        def get_divisors(n):
            divisors = set()
            for i in range(1, int(math.isqrt(n)) + 1):
                if n % i == 0:
                    divisors.add(i)
                    divisors.add(n // i)
            return list(divisors)
        
        divisors = get_divisors(k)
        
        # Use a defaultdict to track groups with default counts initialized for each divisor
        groups = defaultdict(lambda: {d: 0 for d in divisors})
        
        result = 0
        
        for i, num in enumerate(nums):
            group = groups[num]
            current_gcd = math.gcd(i, k)
            t = k // current_gcd
            
            # Add the count of valid previous indices to the result
            if t in group:
                result += group[t]
            
            # Update the divisor counts for current index
            for d in divisors:
                if i % d == 0:
                    group[d] += 1
        
        return result
