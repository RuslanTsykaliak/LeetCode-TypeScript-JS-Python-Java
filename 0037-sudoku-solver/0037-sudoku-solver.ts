/**
 Do not return anything, modify board in-place instead.
 */
function solveSudoku(board: string[][]): void {
    solve(board, 0, 0);
}

function solve(board: string[][], row: number, col: number): boolean {
    if (row === 9) return true;
    if (col === 9) return solve(board, row + 1, 0);

    if (board[row][col] !== '.') return solve(board, row, col + 1);

    for (let num = 1; num <= 9; num++) {
        const char = num.toString();
        if (isValid(board, row, col, char)) {
            board[row][col] = char;
            if (solve(board, row, col + 1)) return true;
            board[row][col] = '.';
        }
    }

    return false;
}

function isValid(board: string[][], row: number, col: number, char: string): boolean {
    for (let i = 0; i < 9; i++) {
        if (board[i][col] === char) return false;
        if (board[row][i] === char) return false;
        if (board[3 * Math.floor(row / 3) + Math.floor(i / 3)][3 * Math.floor(col / 3) + i % 3] === char) return false;
    }
    return true;
}
