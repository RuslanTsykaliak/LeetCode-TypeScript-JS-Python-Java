class Solution {
    public int minOperations(int[] nums, int k) {
        int count = 0;

        for (int i = 0; i < nums.length; i++) {
            if (nums[i] < k) {
                return -1;
            }

            if (nums[i] > k) {
                boolean found = false;
                for (int j = 0; j < i; j++) {
                    if (nums[i] == nums[j]) {
                        found = true;
                        break;
                    }
                }
                if (!found) {
                    count++;
                }
            }
        }
        return count;
    }
}