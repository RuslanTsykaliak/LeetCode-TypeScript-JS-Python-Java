class Solution {
    public int minimumSumSubarray(List<Integer> nums, int l, int r) {
        int minSum = Integer.MAX_VALUE;
        boolean found = false;
        int n = nums.size();

        for (int i = 0; i <= n - l; i++) {
            for (int j = l; j <= r && i + j <= n; j++) {
                int sum = 0;
                for (int k = i; k < i + j; k++) {
                    sum += nums.get(k);
                }
                if (sum > 0) {
                    minSum = Math.min(minSum, sum);
                    found = true;
                }
            }
        }
        return found ? minSum : -1;
    }
}
