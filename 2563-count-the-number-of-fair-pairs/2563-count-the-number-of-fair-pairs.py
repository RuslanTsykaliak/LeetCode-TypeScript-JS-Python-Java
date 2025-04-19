class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        
        def count_less_than(target):
            left, right = 0, len(nums) - 1
            count = 0
            
            while left < right:
                while left < right and nums[left] + nums[right] > target:
                    right -= 1
                # All pairs with indices [left, right] are valid
                count += right - left if left < right else 0
                left += 1
            
            return count
        
        return count_less_than(upper) - count_less_than(lower - 1)