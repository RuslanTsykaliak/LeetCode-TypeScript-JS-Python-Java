class Solution {
    public long countSubarrays(int[] nums, int k) {
        long count = 0;
        int left = 0;
        int window = 0;

        int top = Integer.MIN_VALUE;
        for (int n : nums) {
            if (n > top) {
                top = n;
            }
        }

        for (int right = 0; right < nums.length; right++) {
            if (nums[right] == top) {
                window++;
            }

            while (window >= k) {
                if (nums[left] == top) {
                    window--;
                }
                left++;
            }

            count += left;
        }

        return count;
    }
}