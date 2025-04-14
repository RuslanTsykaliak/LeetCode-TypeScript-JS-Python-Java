function countGoodTriplets(arr: number[], a: number, b: number, c: number): number {
    let count = 0;
    let n = arr.length;

    for (let i = 0; i < n - 2; i++) {
        for (let j = i + 1; j < n - 1; j++) {
            if (Math.abs(arr[i] - arr[j]) > a) continue;
            for (let k = j + 1; k < n; k++) {
                if (Math.abs(arr[j] - arr[k]) > b) continue;
                if (Math.abs(arr[i] - arr[k]) <= c) {
                    count++;
                }
            }
        }
    }
    return count;
};