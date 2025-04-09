/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var minOperations = function(nums, k) {
    // If any number is smaller than k, it's impossible
    if (Math.min(...nums) < k) {
        return -1;
    }

    let uniqueHeights = new Set();

    for (let n of nums) {
        // Only track values greater than k
        if (n > k) {
            uniqueHeights.add(n);
        }
    }
    // Each unique height above k will need a spell to reduce
    return uniqueHeights.size;
};