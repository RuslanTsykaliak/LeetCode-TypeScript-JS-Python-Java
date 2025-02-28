class Solution {
    public int countSubarrays(int[] nums) {
        // What we should return?
        // The number of subarrays of length 3 such that the sum of the first and third
        // numbers equals exactly half of the second number.
        // What are the steps to get result?
        // 1. We declare int result to store result
        int count = 0;
        // 2. We need subarrays of length 3 created from nums
        for (int i = 0; i < nums.length - 2; i++) {
            // 3. We need to add the sum of 1st and 3rd element
            // 4. The sum should be half of the 2nd element
            if ((nums[i] + nums[i + 2]) * 2 == nums[i + 1]) {
                // 5. Increase the count
                count++;
            }
        }
        return count;
    }
}
