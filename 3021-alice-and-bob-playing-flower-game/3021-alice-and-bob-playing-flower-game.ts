class Range {
    constructor(readonly start: number, readonly end: number) {}
    get size() {
        return this.end - this.start + 1;
    }
}

function flowerGame(n: number, m: number): number {
    const rangeN = new Range(1, n);
    const rangeM = new Range(1, m);
    // The number of pairs that can be made from two ranges
    const pairCount = rangeN.size * rangeM.size;

    // for any pair (x, y) x + y must be odd to be counted
    return Math.floor(pairCount / 2);
};