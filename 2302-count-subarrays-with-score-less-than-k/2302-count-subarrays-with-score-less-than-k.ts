function countSubarrays(nums: number[], k: number): number {
    let count = 0;
    let total = 0;
    let left = 0;
    let window = 0;

    for (let right = 0; right < nums.length; right++) {
        total += nums[right];
        window++;

        while ((total * window) >= k) {
            total -= nums[left];
            window--;
            left++;
        }
        count += window;
    }

    return count;
};