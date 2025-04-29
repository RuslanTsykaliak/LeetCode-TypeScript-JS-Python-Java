class Solution {
    public int countSubarrays(int[] nums) {
        // Brute Force
        // int count = 0;

        // for (int i = 0; i < nums.length - 2; i++) {
        //     // nums[i + 1] / 2
        //     if ((nums[i] + nums[i + 2]) * 2 == nums[i + 1]) {
        //         count++;
        //     }
        // }

        // return count;

        int count = 0;
        int l = 0;
        int m = 1;
        int r = 2;


        while (r < nums.length) {
            // doesn't pass nums = [-1,-4,-1,4]
            // if ((nums[l] + nums[r]) == nums[m] / 2) {
            // pass the test
            if ((nums[l] + nums[r]) * 2 == nums[m]) {
                count++;
            }
            l++;
            m++;
            r++;
        }

        return count;
    }
}