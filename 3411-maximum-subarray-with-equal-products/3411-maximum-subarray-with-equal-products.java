class Solution {
    public int maxLength(int[] nums) {
        int maxLength = 0;
        int n = nums.length;

        for (int i = 0; i < n; i++) {
            int prod = 1;
            int gcdVal = nums[i];
            int lcmVal = nums[i];
            for (int j = i; j < n; j++) {
                prod *= nums[j];
                gcdVal = gcd(gcdVal, nums[j]);
                lcmVal = lcm(lcmVal, nums[j]);
                if (prod == (long) lcmVal * gcdVal) {
                    maxLength = Math.max(maxLength, j - i + 1);
                }
            }
        }

        return maxLength;
    }

    private int gcd(int a, int b) {
        return b == 0 ? a : gcd(b, a % b);
    }

    private int lcm(int a, int b) {
        return a * (b / gcd(a, b));
    }
}