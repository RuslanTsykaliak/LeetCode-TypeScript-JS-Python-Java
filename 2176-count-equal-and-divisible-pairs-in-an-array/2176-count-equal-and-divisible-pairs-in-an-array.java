class Solution {
    public int countPairs(int[] nums, int k) {
        int count = 0;
        Map<Integer, List<Integer>> index_map = new HashMap<>();
        for (int j = 0; j < nums.length; j++) {
            int num = nums[j];
            if (index_map.containsKey(num)) {
                for (int i : index_map.get(num)) {
                    if ((long)i * j % k == 0) {
                        count++;
                    }
                }
            }
            index_map.computeIfAbsent(num, key -> new ArrayList<>()).add(j);
        }
        return count;
    }
}