function minimumIndex(nums: number[]): number {
    // 1. Boyer-Moore Majority Voting Algorithm to find the dominant element.
    let majority = 0;
    let count = 0;

    for (let n of nums) {
        if (count === 0) {
            majority = n;
        }
        if (n === majority) {
            count += 1;
        } else {
            count -= 1;
        }
    }

    // 2. Count occurrences of the dominant element in the entire array.
    let right_cnt = nums.filter(n => n === majority).length

    // 3. Iterate to find the minimum valid split index.
    let left_cnt = 0;
    for (let i = 0; i < nums.length - 1; i++) {
        if (nums[i] === majority) {
            left_cnt += 1;
            right_cnt -= 1;
        }

        let left_len = i + 1;
        let right_len = nums.length - i - 1;

        // 4. Check if both left and right subarrays have the same dominant element.
        if (2 * left_cnt > left_len && 2 * right_cnt > right_len) {
            return i;
        }
    }
    // 5. If no valid split is found, return -1.
    return -1;
};