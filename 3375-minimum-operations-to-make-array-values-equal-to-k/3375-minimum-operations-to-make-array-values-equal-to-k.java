class Solution {
    public int minOperations(int[] nums, int k) {
        Set<Integer> uniqueHeights = new HashSet<>();
        for (int n : nums) {
            if (n < k) {
                return -1;
            }
            if (n > k) {
                uniqueHeights.add(n);
            }
        }
        return uniqueHeights.size();
    }
}