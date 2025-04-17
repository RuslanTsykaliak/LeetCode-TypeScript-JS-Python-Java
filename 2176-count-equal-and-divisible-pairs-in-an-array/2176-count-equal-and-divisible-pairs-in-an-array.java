class Solution {
    public int countPairs(int[] nums, int k) {
        int count = 0;
        Map<Integer, List<Integer>> indexMap = new HashMap<>();
        for (int j = 0; j < nums.length; j++) {
            int num = nums[j];
            if (indexMap.containsKey(num)) {
                for (int i : indexMap.get(num)) {
                    if ((long)i * j % k == 0) {
                        count++; // += 1
                    }
                }
            }
            indexMap.computeIfAbsent(num, key -> new ArrayList<>()).add(j);
        }
        return count;
    }
}