function countSubarrays(nums: number[], minK: number, maxK: number): number {
    let answer = 0
    let minKIdx = -1
    let maxKIdx = -1
    let outOfBoundsIdx = -1
    for (let i = 0; i < nums.length; i++) {
        if(nums[i] > maxK || nums[i] < minK) {
            outOfBoundsIdx = i
        }
        if(nums[i] === minK) {
            minKIdx = i
        }
        if(nums[i] === maxK) {
            maxKIdx = i
        }
        answer += Math.max(0, Math.min(minKIdx, maxKIdx) - outOfBoundsIdx)
    }
    return answer
};
