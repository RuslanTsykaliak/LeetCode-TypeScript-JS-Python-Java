class Solution {
    public int tupleSameProduct(int[] nums) {
        // Create a HashMap to store the product of pairs and their frequency
        Map<Integer, Integer> productFrequency = new HashMap<>();

        // Iterate through all possible pairs of integers in the array
        for (int i = 0; i < nums.length; i++) {
            for (int j = i + 1; j < nums.length; j++) {
                int product = nums[i] * nums[j];
                productFrequency.put(product, productFrequency.getOrDefault(product, 0) + 1);
            }
        }

        int count = 0;

        // Calculate the number of valid tuples based on the frequency of the products
        for (int freq : productFrequency.values()) {
            if (freq > 1) {
                count += (freq * (freq - 1)) / 2 * 8;
            }
        }
        return count;
    }
}