function mergeArrays(nums1: number[][], nums2: number[][]): number[][] {
    // Algorithms: HashMap (or Map); Two Pointers (alternative)

    // Input: two 2D integer arrays. Each array contains unique ids and is sorted in ascending order by id.
    // Output: the result array sorted in ascending order by id, containing unique ids and their summed values.

    // 1. Use a Map to store unique ids and their summed values.
    const keyToSum = new Map<number, number>();

    // 2. Populate the Map with values from nums1.
    for (const nums of nums1) {
        keyToSum.set(nums[0], nums[1]);
    }

    // 3. Add values from nums2 to existing keys or create new entries in the Map.
    for (const nums of nums2) {
        const currentSum = keyToSum.get(nums[0]) || 0; // Get existing sum or 0 if key doesn't exist.
        keyToSum.set(nums[0], currentSum + nums[1]);
    }

    // 4. Convert the Map to a 2D array and sort it by id.
    const mergedArray: number[][] = Array.from(keyToSum.entries()).sort((a, b) => a[0] - b[0]);

    return mergedArray;
};