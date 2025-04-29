class Solution {
    public long countSubarrays(int[] nums, long k) {
        long count = 0;
        long total = 0;
        
        int left = 0;
        int window = 0;

        for (int right = 0; right < nums.length; right++) {
            total += nums[right];
            window++;

            while ((total * window) >= k) {
                total -= nums[left];
                window--;
                left++;
            }
            count += window;
        }

        return count;
    }
}