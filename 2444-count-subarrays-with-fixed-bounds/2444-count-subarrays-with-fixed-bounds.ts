function countSubarrays(nums: number[], minK: number, maxK: number): number {
    // Sliding Window
    // Time Complexity O(n)
    // Space Complexity O(1)

    let count = 0;
    let minKIdx = -1, maxKIdx = -1, outOfBoundsIdx = -1;

    for (let i = 0; i < nums.length; i++) {
        const v = nums[i];

        if (v < minK || v > maxK) {
            outOfBoundsIdx = i;
        }

        if (v === minK) {
            minKIdx = i;
        }

        if (v === maxK) {
            maxKIdx = i;
        }

        const validStart = Math.min(minKIdx, maxKIdx);
        count += Math.max(0, validStart - outOfBoundsIdx);
    }

    return count;
};