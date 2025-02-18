class Solution {
    public int maximumDifference(int[] nums) {
        int maxDiff = 0;
        int minDiff = nums[0];

        for (int n : nums) {
            maxDiff = Math.max(maxDiff, n - minDiff);
            minDiff = Math.min(minDiff, n);
        }
        if (maxDiff != 0)
            return maxDiff;
        else
            return -1;
    }
}