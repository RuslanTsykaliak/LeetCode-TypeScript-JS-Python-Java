class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        # Algorithms: Sliding Window
        # Data Structure: Hash Map
        subarrayCount = 0
        n = len(nums)
        pairCount = 0
        start = 0
        numFreq = defaultdict(int)

        for end in range(n):
            num = nums[end]
            pairCount += numFreq[num]
            numFreq[num] += 1

            while pairCount >= k:
                subarrayCount += n - end
                numFreq[nums[start]] -= 1
                pairCount -= numFreq[nums[start]]
                start += 1

        return subarrayCount