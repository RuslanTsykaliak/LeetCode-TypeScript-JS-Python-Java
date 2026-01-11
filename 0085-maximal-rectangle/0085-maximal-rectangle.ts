function maximalRectangle(matrix: string[][]): number {
    if (matrix.length === 0) return 0;

    const rows = matrix.length;
    const cols = matrix[0].length;
    const heights = new Array<number>(cols).fill(0);
    let maxArea = 0;

    for (let r = 0; r < rows; r++) {
        // Build histogram for current row
        for (let c = 0; c < cols; c++) {
            heights[c] = matrix[r][c] === "1" ? heights[c] + 1 : 0;
        }

        maxArea = Math.max(maxArea, largestRectangleArea(heights));
    }

    return maxArea;
}

function largestRectangleArea(heights: number[]): number {
    const stack: number[] = [];
    let maxArea = 0;
    const extendedHeights = [...heights, 0];

    for (let i = 0; i < extendedHeights.length; i++) {
        while (
            stack.length > 0 &&
            extendedHeights[i] < extendedHeights[stack[stack.length - 1]]
        ) {
            const height = extendedHeights[stack.pop()!];
            const width =
                stack.length === 0 ? i : i - stack[stack.length - 1] - 1;
            maxArea = Math.max(maxArea, height * width);
        }

        stack.push(i);
    }

    return maxArea;
}