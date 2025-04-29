function countSubarrays(nums: number[]): number {
    let count = 0;

    for (let i = 0; i < nums.length - 2; i++) {
        let m = i + 1;
        let r = i + 2;
        if ((nums[i] + nums[r]) * 2 === nums[m]) {
            count++;
        }
    }

    return count;
};