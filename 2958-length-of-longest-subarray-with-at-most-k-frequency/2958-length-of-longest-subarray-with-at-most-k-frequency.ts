function maxSubarrayLength(nums: number[], k: number): number {
    const frequencyMap: Map<number, number> = new Map()
    let maxLength = 0
    let start = 0
    let end = 0

    for (end = 0; end < nums.length; ++end) {
        frequencyMap.set(nums[end], (frequencyMap.get(nums[end]) ?? 0) + 1)
        while (frequencyMap.get(nums[end])! > k) {
            frequencyMap.set(nums[start], frequencyMap.get(nums[start])! - 1)
            ++start
        }
        maxLength = Math.max(maxLength, end - start + 1)
    }

    return maxLength
};