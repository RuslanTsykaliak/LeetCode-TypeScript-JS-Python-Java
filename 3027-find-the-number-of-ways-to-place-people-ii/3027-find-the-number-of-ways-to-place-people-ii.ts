function numberOfPairs(points: number[][]): number {
    points.sort((a, b) => a[0] - b[0] || b[1] - a[1]);
    let result = 0, l = points.length;

    for (let i = 0; i < l - 1; i++) {
        let xLow = points[i][0] - 1, yLow = -Infinity;
        const xHigh = Infinity, yHigh = points[i][1] + 1;
        for (let j = i + 1; j < l; j++) {
            if (
                points[j][0] > xLow && points[j][0] < xHigh &&
                points[j][1] > yLow && points[j][1] < yHigh
            ) {
                result++, xLow = points[j][0], yLow = points[j][1];
            }
        }
    }
    return result;
};