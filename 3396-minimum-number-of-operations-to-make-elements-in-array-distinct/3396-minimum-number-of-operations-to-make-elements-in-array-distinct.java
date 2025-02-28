class Solution {
    public int minimumOperations(int[] nums) {
        int count = 0;
        Set<Integer> distinct = new HashSet<>();
        int index = 0;

        while (index < nums.length) {
            distinct.clear();
            boolean allDistinct = true;

            for (int i = index; i < nums.length; i++) {
                if (distinct.contains(nums[i])) {
                    allDistinct = false;
                    break;
                } else {
                    distinct.add(nums[i]);
                }
            }

            if (allDistinct) {
                break;
            } else {
                count++;
                index += 3;
            }
        }

        return count;
    }
}
