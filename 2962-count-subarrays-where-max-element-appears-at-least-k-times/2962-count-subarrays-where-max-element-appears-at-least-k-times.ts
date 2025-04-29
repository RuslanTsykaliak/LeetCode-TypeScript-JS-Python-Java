function countSubarrays(nums: number[], k: number): number {
    let count = 0;
    let left = 0;
    let window = 0;
    const top = Math.max(...nums);

    for (let right = 0; right < nums.length; right++) {
        if (nums[right] === top) {
            window++;
        }

        while (window >= k) {
            if (nums[left] === top) {
                window--;
            }
            left++;
        }
        count += left;
    }


    return count;
};