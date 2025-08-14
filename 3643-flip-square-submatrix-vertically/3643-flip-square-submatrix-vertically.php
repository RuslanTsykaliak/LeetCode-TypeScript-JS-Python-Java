class Solution {

    /**
     * @param Integer[][] $grid
     * @param Integer $x
     * @param Integer $y
     * @param Integer $k
     * @return Integer[][]
     */
    function reverseSubmatrix($grid, $x, $y, $k) {
        # The goal is to reverse rows in the square

        # We will need to indentify the top and bottom rows
        $top = $x;
        $bottom = $x + $k - 1;

        # We can use loop to swap rows from top to bottom
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