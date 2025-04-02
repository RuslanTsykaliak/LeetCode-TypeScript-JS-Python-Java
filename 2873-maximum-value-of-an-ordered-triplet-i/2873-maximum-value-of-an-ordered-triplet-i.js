/**
 * @param {number[]} nums
 * @return {number}
 */
var maximumTripletValue = function(nums) {
    let res = 0, diff = 0, left = 0

    for (const i of nums) {
        res = Math.max(res, diff * i)
        diff = Math.max(diff, left - i)
        left = Math.max(left, i)
    }
    return res
    
};