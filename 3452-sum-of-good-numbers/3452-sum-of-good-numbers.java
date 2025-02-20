class Solution {
    public int sumOfGoodNumbers(int[] nums, int k) {
        int sum = 0;
        int n = nums.length;

        for (int i = 0; i < n; i++) {
            // Assume it's good initially
            boolean isGood = true;

            // Check left; if NOT greater, it's NOT good
            if (i - k >= 0 && nums[i] <= nums[i - k]) {
                isGood = false;
            }

            // Check right; if NOT greater, it's NOT good
            if (i + k < n && nums[i] <= nums[i + k]) {
                isGood = false;
            }
            // Add to sum ONLY if it's still considered good
            if (isGood) {
                sum += nums[i];
            }
        }
        return sum;
    }
}