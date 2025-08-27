type Matrix = Array<Array<number>>;

class Coord {
    i: number;
    j: number;

    static directions: Array<Coord> = [
        new Coord(-1, -1), // top-left
        new Coord(-1, 1), // top-right
        new Coord(1, 1), // bottom-right
        new Coord(1, -1), // bottom-left
    ];

    constructor(i: number, j: number) {
        this.i = i;
        this.j = j;
    }

    add(delta: Coord): Coord {
        return new Coord(this.i + delta.i, this.j + delta.j);
    }

    invert(): Coord {
        return new Coord(-this.i, -this.j);
    }

    checkBounds(max: Coord): boolean {
        return this.i >= 0 &&
            this.j >= 0 &&
            this.i < max.i &&
            this.j < max.j;
    }

    getValue(matrix: Matrix): number {
        return matrix[this.i][this.j];
    }
}

function matrixMax(matrix: Matrix, mapFn: (value: number, coord: Coord) => number): number {
    const n = matrix.length;
    const m = matrix[0].length;
    let max = -Infinity;
    for (let i = 0; i < n; i++) {
        for (let j = 0; j < m; j++) {
            const result = mapFn(matrix[i][j], new Coord(i, j));
            max = Math.max(max, result);
        }
    }
    return max;
}

const NO_TURN = 0;
const TURN = 1;
const TURN_OPTIONS = 2;

const DIRECTION_OPTIONS = Coord.directions.length;

const START_VALUE = 1;

const expectedValueMap = [
    2, // 2 after 0
    2, // 2 after 1
    0, // 0 after 2
];

function clockwiseTurn(directionIndex: number): number {
    return (directionIndex + 1) % DIRECTION_OPTIONS;
}

function lenOfVDiagonal(grid: Matrix): number {
    const bounds = new Coord(grid.length, grid[0].length);

    function memo<T>(fn: T): T {
        const cache = new Array(bounds.i * bounds.j * TURN_OPTIONS * DIRECTION_OPTIONS);
        return (((c: Coord, turn: number, directionIndex: number) => {
            const hash = (c.i * bounds.j + c.j) * TURN_OPTIONS * DIRECTION_OPTIONS +
                turn * DIRECTION_OPTIONS +
                directionIndex;
            const value = cache[hash];
            if (value !== undefined) {
                return value;
            }
            const result = (fn as any)(c, turn, directionIndex);
            cache[hash] = result;
            return result;
        }) as any) as T;
    }

    const dp = memo((coord: Coord, turn: number, directionIndex: number) => {
        const direction = Coord.directions[directionIndex];
        const prevCoord = coord.add(direction.invert());
        const prevValue = prevCoord.getValue(grid);
        const expectedValue = expectedValueMap[prevValue];
        const value = coord.getValue(grid);
        if (value !== expectedValue) {
            return 0;
        }
        const nextCoord = coord.add(direction);
        const nextResult = nextCoord.checkBounds(bounds) ?
            1 + dp(nextCoord, turn, directionIndex) :
            1;
        let turnResult = 1;
        if (turn) {
            const turnDirectionIndex = clockwiseTurn(directionIndex);
            const turnCoord = coord.add(Coord.directions[turnDirectionIndex]);
            if (turnCoord.checkBounds(bounds)) {
                turnResult = 1 + dp(turnCoord, NO_TURN, turnDirectionIndex);
            }
        }
        return Math.max(nextResult, turnResult);
    });

    return matrixMax(grid, (value, coord) => {
        if (value !== START_VALUE) {
            return 0;
        }
        return 1 + Math.max(
            ...Coord.directions.map((direction, i) => {
                const nextCoord = coord.add(direction);
                if (nextCoord.checkBounds(bounds)) {
                    return dp(nextCoord, TURN, i);
                }
                return 0;
            })
        );
    });
};