/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var countSubarrays = function(nums, k) {
    let count = 0;
    let top = Math.max(...nums);
    let left = 0;
    let window = 0;

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