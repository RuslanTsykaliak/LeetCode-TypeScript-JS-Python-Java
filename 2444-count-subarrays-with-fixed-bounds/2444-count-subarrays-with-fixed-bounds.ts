function countSubarrays(nums: number[], minK: number, maxK: number): number {
    let count = 0, minKIdx = -1, maxKIdx = -1, outOfBoundsIdx = -1;
    for (let i = 0; i < nums.length; i++) {
        if (nums[i] > maxK || nums[i] < minK) {
            outOfBoundsIdx = i;
        }
        if (nums[i] === minK) {
            minKIdx = i;
        }
        if (nums[i] === maxK) {
            maxKIdx = i
        }
        count += Math.max(0, Math.min(minKIdx, maxKIdx) - outOfBoundsIdx);
    }
    return count;
};