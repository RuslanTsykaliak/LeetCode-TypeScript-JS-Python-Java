class Solution {
    public int maximumDifference(int[] nums) {
        int maxDiff = 0;
        int minVal = nums[0];

        for (int n : nums) {
            maxDiff = Math.max(maxDiff, n - minVal);
            minVal = Math.min(minVal, n);
        }

        if (maxDiff == 0) {
            return -1;
        } else {
            return maxDiff;
        }
    }
}