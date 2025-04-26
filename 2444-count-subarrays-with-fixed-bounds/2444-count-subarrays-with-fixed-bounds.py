class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        count = 0
        minIdx = -1
        maxIdx = -1
        outIdx = -1

        for i in range(len(nums)):
            num = nums[i]

            if num < minK or num > maxK:
                outIdx = i

            if num == minK:
                minIdx = i

            if num == maxK:
                maxIdx = i
            
            validStart = min(minIdx, maxIdx)

            if validStart > outIdx:
                count += validStart - outIdx
        
        return count