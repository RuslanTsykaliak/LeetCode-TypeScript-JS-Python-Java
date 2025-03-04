function sumOfGoodNumbers(nums: number[], k: number): number {
    let sum = 0;
    let n = nums.length;

    for (let i = 0; i < n; i++) {
        let isGood:boolean = true;

        // Check left; if NOT greater, it's NOT good
        if (i - k >= 0 && nums[i] <= nums[i - k]) {
            isGood = false;
        }

        // Check right; if NOT greater, it's NOT good
        if (i + k < n && nums[i] <= nums[i + k]) {
            isGood = false;
        }

        // Add to sum ONLY if it's still considered good
        if (isGood) {
            sum += nums[i];
        }
    }
    return sum;
};