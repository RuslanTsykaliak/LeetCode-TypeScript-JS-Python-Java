class Solution {
    public List<Integer> targetIndices(int[] nums, int target) {
        // We are given an array, that should be sorted
        Arrays.sort(nums);
        // We are given the target number
        // Output: return the list of the indecis where the value the same as the target or if non found return an empty list.
        List<Integer> indices = new ArrayList<>();

        // For lop, the logic will be to compare numbers in the sorted array to the targeted number. Then, update array with indecies if any and return array
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] == target) {
                indices.add(i);
            }
        }
        return indices;
    }
}