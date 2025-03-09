class Solution {
    public int[] applyOperations(int[] nums) {
        int n = nums.length;

        for (int i = 1; i < n; i++) {
            if (nums[i] != 0 && nums[i - 1] == nums[i]) {
                nums[i - 1] *= 2;
                nums[i] = 0;
            }
        }

        for (int i = 0, j = 0; j < n; j++) {
            if (nums[j] != 0) {
                if (i < j) {
                    int temp = nums[i];
                    nums[i] = nums[j];
                    nums[j] = temp;
                }
                i++;
            }
        }
        return nums;
    }
}