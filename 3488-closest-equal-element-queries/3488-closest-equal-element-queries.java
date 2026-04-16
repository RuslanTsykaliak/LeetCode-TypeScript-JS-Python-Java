class Solution {
    public List<Integer> solveQueries(int[] nums, int[] queries) {
        int n = nums.length;
        int[] left = new int[n];
        int[] right = new int[n];

        HashMap<Integer, Integer> pos = new HashMap<>();
        for (int i = -n; i < n; i++) {
            if (i >= 0) {
                left[i] = pos.getOrDefault(nums[i], i - n);
            }
            pos.put(nums[((i % n) + n) % n], i);
        }

        pos.clear();
        for (int i = 2 * n - 1; i >= 0; i--) {
            if (i < n) {
                right[i] = pos.getOrDefault(nums[i], i + n);
            }
            pos.put(nums[i % n], i);
        }

        List<Integer> result = new ArrayList<>();
        for (int i = 0; i < queries.length; i++) {
            int x = queries[i];
            if (x - left[x] == n) {
                result.add(-1);
            } else {
                result.add(Math.min(x - left[x], right[x] - x));
            }
        }
        return result;
    }
}