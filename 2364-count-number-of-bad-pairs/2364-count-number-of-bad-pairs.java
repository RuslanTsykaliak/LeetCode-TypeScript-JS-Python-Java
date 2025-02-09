class Solution {
    public long countBadPairs(int[] nums) {
        long count = 0;
        int n = nums.length;

        for (int i = 0; i < n; i++) {
            nums[i] = i - nums[i];
        }

        Map<Integer, Integer> d = new HashMap();

        for (int num : nums) {
            count = (count + d.getOrDefault(num, 0));
            d.put(num, d.getOrDefault(num, 0) + 1);
        }
        return 1L * n * (n - 1) / 2 - count;
    }
}