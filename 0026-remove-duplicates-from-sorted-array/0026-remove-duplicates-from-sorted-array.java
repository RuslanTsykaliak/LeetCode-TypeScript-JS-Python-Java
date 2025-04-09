class Solution {
    public int removeDuplicates(int[] nums) {
        Set unique = new HashSet<Integer>();
        int k = 0;

        for (int n : nums) {
            if (!unique.contains(n)) {
                unique.add(n);
                nums[k] = n;
                k++;
            }
        }
        return k;
    }
}