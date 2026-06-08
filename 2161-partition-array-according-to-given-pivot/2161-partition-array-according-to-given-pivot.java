class Solution {
    public int[] pivotArray(int[] nums, int pivot) {
        int n = nums.length;
        int[] result = new int[n];
        int lessI = 0;
        int greaterI = n - 1;

        for (int i = 0, j = n - 1; i < n; i++, j--) {
            if (nums[i] < pivot) {
                result[lessI] = nums[i];
                lessI++;
            }
            if (nums[j] > pivot) {
                result[greaterI] = nums[j];
                greaterI--;
            }
        }
        while (lessI <= greaterI) {
            result[lessI] = pivot;
            lessI++;
        }
        return result;
    }
}