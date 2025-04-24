class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        total_unique = len(set(nums))
        freq = {}
        left = 0
        count = 0

        for right, v in enumerate(nums):
            freq[v] = freq.get(v, 0) + 1

            while len(freq) == total_unique:
                count += n - right
                freq[nums[left]] -= 1
                if freq[nums[left]] == 0:
                    del freq[nums[left]]
                left += 1
        
        return count