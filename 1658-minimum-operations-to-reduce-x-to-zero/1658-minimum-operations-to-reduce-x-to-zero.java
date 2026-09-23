class Solution {
    public int minOperations(int[] nums, int x) {
        int arraysum = 0;
        for (int i = 0; i < nums.length; i++) {
            arraysum += nums[i];
        }
        int remsum = arraysum - x;
        int answer = maxsizesubarray(nums, remsum);
        return (answer == -1) ? -1 : nums.length - answer;
    }

    public int maxsizesubarray(int[] arr, int target) {
        int result = -1;
        int left = 0;
        int right = 0;
        int sum = 0;
        while (right < arr.length) {
            sum += arr[right];
            while (sum > target && left != arr.length) {
                sum -= arr[left++];
            }
            if (sum == target) {
                result = Math.max(result, right + 1 - left);
            }
            right++;
        }
        return (int) result;
    }
}