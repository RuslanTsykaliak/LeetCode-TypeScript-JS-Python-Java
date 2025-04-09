function minOperations(nums: number[], k: number): number {
    // HashSet()
    let h = new Set<number>();

    for (let n of nums) {
        if (n < k) {
            return -1;
        }
        h.add(n)l
    }
    return h.has(k) ? h.size - 1 : h.size;
};