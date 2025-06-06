class Solution {
    public int[] findThePrefixCommonArray(int[] A, int[] B) {
        int n = A.length;
        int[] prefixCommonArray = new int[n];

        // Loop through each index to calculate common elements for each prefix
        for (int currentI = 0; currentI < n; ++currentI) {
            int commonCount = 0;

            // Compare elements in A and B within the range of current prefix
            for (int aI = 0; aI <= currentI; ++aI) {
                for (int bI = 0; bI <= currentI; ++bI) {
                    // Check if elements match, and count if they do
                    if (A[aI] == B[bI]) {
                        ++commonCount;
                        break; // Prevent counting duplicates
                    }
                }
            }
            // Store the count of common elements for the current prefix
            prefixCommonArray[currentI] = commonCount;
        }
        // Return the final array with counts of common elements in each prefix
        return prefixCommonArray;
    }
}