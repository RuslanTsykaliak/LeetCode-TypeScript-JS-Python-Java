class Solution {
    public void moveZeroes(int[] nums) {
        int n = nums.length;
        if (nums == null || n == 0)
            return;

        int insert = 0;
        for (int num : nums) {
            if (num != 0) {
                nums[insert++] = num;
            }
        }

        while (insert < n) {
            nums[insert++] = 0;
        }
    }
}