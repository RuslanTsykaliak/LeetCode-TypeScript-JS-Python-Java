function subsetXORSum(nums: number[]): number {
    // Algorithm: Bit Manipulation
    let res = 0;

    for (let n of nums) {
        res |= n;
    }

    return res * 2 ** (nums.length - 1)
};