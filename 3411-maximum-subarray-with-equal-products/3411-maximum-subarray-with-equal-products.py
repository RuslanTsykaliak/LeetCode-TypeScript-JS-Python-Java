class Solution:
    def maxLength(self, nums: List[int]) -> int:
        maxLength = 0
        n = len(nums)
        

        for i in range(n):
            prod = 1
            gcdVal = nums[i]
            lcmVal = nums[i]
            j = 1
            prod *= nums[j]
            gcdVal = gcd(gcdVal, nums[j])
            lcmVal = lcm(lcmVal, nums[j])
            if prod == lcmVal * gcdVal:
                maxLength = max(maxLength, j - i + 1)
        return maxLength

