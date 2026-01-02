class Solution {
    public int repeatedNTimes(int[] nums) {
        Map<Integer, Integer> count = new HashMap();
        for (int x : nums) {
            count.put(x, count.getOrDefault(x, 0) + 1);
        }

        for (int k : count.keySet()) {
            if (count.get(k) > 1) {
                return k;
            }
        }

        throw null;
    }
}