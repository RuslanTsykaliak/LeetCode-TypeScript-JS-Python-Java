class Spreadsheet {

    grid: number[][] = [];

    constructor(rows: number) {

        for (let r = 0; r < rows; r++) {
            this.grid[r] = [];
            for (let c = 0; c < 26; c++) {
                this.grid[r][c] = 0;
            }
        }
    }

    setCell(cell: string, value: number): void {

        const [r, c] = this.getCoords(cell);
        this.grid[r][c] = value;
    }

    resetCell(cell: string): void {
        const [r, c] = this.getCoords(cell);
        this.grid[r][c] = 0;
    }

    getValue(formula: string): number {
        const f = formula.substring(1);
        const [x, y] = f.split('+');

        let v0 = 0;
        let v1 = 0;

        if (this.isNumber(x)) {
            v0 = parseInt(x);
        } else {
            const [xr, xc] = this.getCoords(x);
            v0 = this.grid[xr][xc];
        }

        if (this.isNumber(y)) {
            v1 = parseInt(y);
        } else {
            const [yr, yc] = this.getCoords(y);
            v1 = this.grid[yr][yc];
        }

        const v = v0 + v1;

        return v;
    }

    private getCoords(cell: string): [number, number] {
        const [label, row] = cell.split(/(\d+)/);
        const col = label.charCodeAt(0) - 65;

        return [parseInt(row) - 1, col];
    }

    private isNumber(n: string) {
        return !Number.isNaN(parseInt(n, 10));
    }
}