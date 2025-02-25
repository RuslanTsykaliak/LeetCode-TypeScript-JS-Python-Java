class Solution {
    public int maxAdjacentDistance(int[] nums) {
        int maxDiff = 0;

        for (int i = 0; i < nums.length; i++) {
            int diff = Math.abs(nums[i] - nums[(i + 1) % nums.length]);
            maxDiff = Math.max(maxDiff, diff);
        }

        return maxDiff;
    }
}