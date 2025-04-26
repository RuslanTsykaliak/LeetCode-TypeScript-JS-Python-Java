function countSubarrays(nums: number[], minK: number, maxK: number): number {
    let count = 0;
    // Track last indices of minK, maxK, and any value outside [minK, maxK]
    let minKIdx = -1, maxKIdx = -1, outOfBoundsIdx = -1;

    for (let i = 0; i < nums.length; i++) {
        const v = nums[i];

        // If v is out of the allowed range, reset the window
        if (v < minK || v > maxK) {
            outOfBoundsIdx = i;
        }
        // Record when we see minK or maxK
        if (v === minK) {
            minKIdx = i;
        }
        if (v === maxK) {
            maxKIdx = i;
        }

        // Earliest start that includes both minK and maxK
        const validStart = Math.min(minKIdx, maxKIdx);
        // All starts after outOfBoundsIdx up to validStart are valid
        count += Math.max(0, validStart - outOfBoundsIdx);
    }

    return count;
};