class Solution {
    public int minimumOperations(int[] nums) {
        if (nums.length == 0) {
            return 0;
        }

        boolean[] seen = new boolean[101];

        for (int i = nums.length - 1; i >= 0; i--) {
            if (seen[nums[i]]) {
                return i / 3 + 1;
            } else {
                seen[nums[i]] = true;
            }
        }
        return 0;
    }
}