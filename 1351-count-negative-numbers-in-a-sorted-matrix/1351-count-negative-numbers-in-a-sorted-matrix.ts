function countNegatives(grid: number[][]): number {
    return grid.flat().filter(el => el < 0).length
};