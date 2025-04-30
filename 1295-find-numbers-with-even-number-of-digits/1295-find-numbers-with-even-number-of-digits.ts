function findNumbers(nums: number[]): number {
    let count = 0;

    for (const n of nums) {
        if (n.toString().length % 2 === 0) {
            count++;
        }
    }

    return count;
};