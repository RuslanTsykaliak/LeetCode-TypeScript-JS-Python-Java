class Solution {

    /**
     * @param Integer[][] $grid
     * @return Integer
     */
    function minimumArea($grid) {
        $rows = count($grid);
        if ($rows === 0) return 0;
        $cols = count($grid[0]);
        if ($cols === 0) return 0;

        // Initialize variables to track the min and max row and column indices containing '1'
        $minRow = $rows;
        $maxRow = -1;
        $minCol = $cols;
        $maxCol = -1;

        // Single pass through the grid to find the extreme coordinates of '1's
        for ($r = 0; $r < $rows; $r++) {
            for ($c = 0; $c < $cols; $c++) {
                if ($grid[$r][$c] === 1) {
                    $minRow = min($minRow, $r);
                    $maxRow = max($maxRow, $r);
                    $minCol = min($minCol, $c);
                    $maxCol = max($maxCol, $c);
                }
            }
        }

        // If no '1's were found, return 0
        if ($maxRow === -1 || $maxCol === -1) return 0;

        // Calculate the height and width of the rectangle
        $height = $maxRow - $minRow + 1;
        $width = $maxCol - $minCol + 1;

        // Return the area of the rectangle
        return $height * $width;
    }
}