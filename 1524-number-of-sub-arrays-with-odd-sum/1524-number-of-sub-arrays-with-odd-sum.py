class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
        MOD = 10**9 + 7
        count, prefixSum, oddCount = 0, 0, 0
        # evenCount starts as one since the initial sum (0) is even
        evenCount = 1

        for num in arr:
            prefixSum += num
            # If current prefix sum is even, add the number of odd subarrays
            if prefixSum % 2 == 0:
                count += oddCount
                evenCount += 1
            else:
                # If current prefix sum is odd, add the number of even subarrays
                count += evenCount
                oddCount += 1
            
            count %= MOD # To handle large results by dividing them
        
        return count

