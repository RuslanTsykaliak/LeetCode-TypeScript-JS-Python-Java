class Solution {
    public int countSubarrays(int[] nums) {
        // Brute Force
        int count = 0;

        for (int i = 0; i < nums.length - 2; i++) {
            // nums[i + 1] / 2
            if ((nums[i] + nums[i + 2]) * 2 == nums[i + 1]) {
                count++;
            }
        }

        return count;
    }
}