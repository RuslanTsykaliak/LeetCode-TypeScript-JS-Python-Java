class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        # Algorithm: Brute Force
        # Time Complexity O(n^2)

        # Input: array nums and an integer k
        # Output: Count
        # Coditions:
        # nums[i] == nums[j]
        # (i * j) is divisible by k

        # count = 0
        # n = len(nums)
        # for i in range(n - 1):
        #     for j in range(i + 1, n):
        #         # Just copy past explanation part
        #         if nums[i] != nums[j]: continue
        #         if (i * j) % k == 0:
        #             count += 1
        # return count

        #################################################
        # What will be better solution?
        # Hash Map

        # Counter + Module inside of hash map
        # count = 0
        # map = defaultdict(Counter)

        # for i, num in enumerate(nums):
        #     for j in map[num]:
        #         if (i * j) % k == 0:
        #             count += map[num][j]
        #     map[num][i % k] += 1

        # return count


        # Simpler Hash Map

        # index_map = defaultdict(list)
        # result = 0

        # for i in range(len(nums)):
        #     for j in index_map[nums[i]]:
        #         if (i * j) % k == 0:
        #             result += 1

        #     index_map[nums[i]].append(i)

        # return result


        # Trying O(n)
        # count = 0
        # mod_groups = defaultdict(lambda: defaultdict(int))

        # for i, num in enumerate(nums):
        #     i_mod = i % k
        #     for j_mod in range(k):
        #         if (i_mod * j_mod) % k == 0:
        #             count += mod_groups[num][j_mod]
        #     mod_groups[num][i_mod] += 1
        # return count


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
