class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        # Normal explanation 
        # we have an arr = [0,2,3,1]
        # premutation will be equal to values:
        # arr[0],arr[2], arr[3], arr[1]
        # in numbers:
        # 0, 3, 1, 2

        # How to realize it?

        # we can build an answer array
        # ans = []
        

        # # next use for loop to add elements to the ans
        # for i in range(len(nums)):
        #     # assigne value of nums[i] to temp value
        #     temp = nums[i]
        #     # use temp value as index to add int to ans
        #     ans.append(nums[temp])

        # return ans

        # Encoding
        n = len(nums)
        for i in range(n):
            nums[i] = nums[i] + n * (nums[nums[i]] % n)
        
        for i in range(n):
            nums[i] = nums[i] // n
        
        return nums
        











