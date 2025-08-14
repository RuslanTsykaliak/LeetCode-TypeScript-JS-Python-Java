class Solution {

    /**
     * @param Integer[][] $grid
     * @param Integer $x
     * @param Integer $y
     * @param Integer $k
     * @return Integer[][]
     */
    function reverseSubmatrix($grid, $x, $y, $k) {
        // The goal is to replace the top row with the bottom row inside of the grid and then return the updated grid.
        // We can declare top and bottom variables to hold row indices from top to button. Then run a nested while and for loops:
        // the first one will update the rows, and the second will update the numbres inside of the grid.

        // Declare $top and $bottom variables
        $top = $x;
        $bottom = $x + $k - 1;

        // Run the nested loop to swap rows
        while ($top < $bottom) {
            for ($i = 0; $i < $k; $i++) {
                $temp = $grid[$top][$y + $i];
                $grid[$top][$y + $i] = $grid[$bottom][$y + $i];
                $grid[$bottom][$y + $i] = $temp;
            }
            $top++;
            $bottom--;
        }
        return $grid;
    }
}