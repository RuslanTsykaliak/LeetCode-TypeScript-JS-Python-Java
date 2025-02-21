class Solution {
    public int[] runningSum(int[] nums) {
        // 1. Create a storage array for the running sums
        int[] sumArray = new int[nums.length];
        int sum = 0;

        // 2. Iterate through all elements in nums
        for (int i = 0; i < nums.length; i++) {
            // Add the current element to the running sum and store it in sumArray
            sum += nums[i];
            sumArray[i] = sum;
        }
        return sumArray;
    }
}
