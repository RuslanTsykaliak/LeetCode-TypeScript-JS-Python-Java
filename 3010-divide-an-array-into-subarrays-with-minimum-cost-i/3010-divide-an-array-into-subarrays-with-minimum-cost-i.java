class Solution {
    public int minimumCost(int[] nums) {
        int n = nums.length;
        int f = nums[0];
        int[] rem = Arrays.copyOfRange(nums, 1, n);
        Arrays.sort(rem);
        return f + rem[0] + rem[1];
    }
}