class Solution {
    public int[][] mergeArrays(int[][] nums1, int[][] nums2) {
        Map<Integer, Integer> keyToSum = new TreeMap<>();

        // Copying the array nums1 to the map
        for (int[] n : nums1) {
            keyToSum.put(n[0], n[1]);
        }

        // Adding the values to existing keys or create new entries
        for (int[] n : nums2) {
            keyToSum.put(n[0], keyToSum.getOrDefault(n[0], 0) + n[1]);
        }

        List<int[]> mergedList = new ArrayList<>();
        for (Map.Entry<Integer, Integer> entry : keyToSum.entrySet()) {
            mergedList.add(new int[] { entry.getKey(), entry.getValue() });
        }

        // Convert the mergedList to int[][] array
        int[][] mergedArray = new int[mergedList.size()][2];
        for (int i = 0; i < mergedList.size(); i++) {
            mergedArray[i] = mergedList.get(i);
        }

        return mergedArray;
    }
}