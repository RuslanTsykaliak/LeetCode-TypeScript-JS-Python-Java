class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        # Topics: 
            # Array 
            # Two Pointers
            # Sorting
        
        # Input: an array of integers
        # Output: the array of itegers
        # Coditions: 
        # integers should be moved, even to the start (left) of the array,
        # odd to the end (right)
        # Order doesn't metter.

        # Algorithms: 
        # We can sort them in palce or we can create a new array and add them.

        # Create a new array and add integers using for-loop
        n = len(nums)
        res = [0] * n
        even = 0
        odd = n - 1
        for num in nums:
            if num % 2 == 0:
                # we add integer to the beggining of the array
                res[even] = num
                even += 1
            else:
                # we add integer to the end of the array
                res[odd] = num
                odd -= 1
        return res
