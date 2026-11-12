class Solution {
    public int longestMonotonicSubarray(int[] nums) {
        // Track current lengths of increasing and decreasing sequences
        int incLength = 1, decLength = 1;
        int maxLength = 1;

        // Iterate through array comparing adjacent elements
        for (int i = 0; i < nums.length - 1; i++) {
            if (nums[i + 1] > nums[i]) {
                // If next element is larger, extend increasing sequence
                incLength++;
                decLength = 1; // Reset decreasing sequence
                maxLength = Math.max(maxLength, incLength);
            } else if (nums[i + 1] < nums[i]) {
                // If next element is smaller, extend decreasing sequence
                decLength++;
                incLength = 1; // Reset increasing sequence
                maxLength = Math.max(maxLength, decLength);
            } else {
                // If elements are equal, reset both sequences
                incLength = 1;
                decLength = 1;
            }
        }
        return maxLength;
    }
}