function longestSubarray(nums: number[]): number {
    let maxLength = 0;
    let count = 0;
    let onesBefore = 0;
    for (const num of nums) {
        if (num) {
            count++;
            maxLength = Math.max(maxLength, count + onesBefore);
        } else {
            onesBefore = count;
            count = 0;
        }
    }
    return Math.min(maxLength, nums.length - 1);
};