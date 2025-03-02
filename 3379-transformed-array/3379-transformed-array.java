class Solution {
    public int[] constructTransformedArray(int[] nums) {
        int n = nums.length;
        int[] result = new int[n];

        for (int i = 0; i < n; i++) {
            if (nums[i] == 0) {
                result[i] = 0;
            } else if (nums[i] < 0) {
                int minus = Math.abs(nums[i]) % n;
                int j = i - minus;
                if (j >= 0) {
                    result[i] = nums[j];
                } else {
                    result[i] = nums[n + j];
                }
            } else {
                int add = nums[i] % n;
                result[i] = nums[(i + add) % n];
            }
        }
        return result;
    }
}