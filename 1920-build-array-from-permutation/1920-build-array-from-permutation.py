class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        # nums = [0, 2, 3, 1]
        # nums[nums[i]] 
        # idex 0 = 0
        # idex 1 = 2
        # idex 2 = 3
        # idex 3 = 1

        # ans = [0, 3, 1, 2]

        # Algorithms Array Traversal, Mathematical Econding
        # Data Structure: Array
        # Time Complexity & Space Complexity:
        # Both solutions: O(n) time complexity
        # Array Traversal: O(n) space complexity
        # Mathematical Encoding: O(1) (in-pace modification)

        # Array Traversal
        ans = []
        for i in range(len(nums)):
            temp = nums[i]
            ans.append(nums[temp])
        return ans
        