class Solution {
    public int countValidSelections(int[] nums) {
        int result = 0;
        int n = nums.length;
        int[] left = new int[n];
        int[] right = new int[n];

        for (int i = 1; i < n; ++i) {
            left[i] = left[i - 1] + nums[i - 1];
            right[n - i - 1] = right[n - i] + nums[n - i];
        }

        for (int i = 0; i < n; ++i) {
            if (nums[i] != 0) {
                continue;
            }
            if (left[i] == right[i]) {
                result += 2;
            }
            if (Math.abs(left[i] - right[i]) == 1) {
                result += 1;
            }
        }
        return result;
    }
}