class Solution {
    public int waysToSplitArray(int[] nums) {
        long sum = 0;

        for (int i : nums) {
            sum += i;
        }

        long currSum = 0;
        int res = 0;

        for (int i = 0; i < nums.length - 1; i++) {
            currSum += nums[i];
            if (2 * currSum >= sum) {
                res++;
            }
        }
        return res;
    }
}