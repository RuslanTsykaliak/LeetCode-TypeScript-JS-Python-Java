class Solution {

    /**
     * @param Integer[] $height
     * @return Integer
     */
    function maxArea($h) {
        $mA = 0; // Maximum area
        $i = 0; // Left pointer
        $y = count($h) - 1; // Right pointer

        while ($i < $y) {
            // Calculate current area
            $mA = max(($y - $i) * min($h[$i], $h[$y]), $mA);

            // Move the pointer pointing to the shorter line
            if ($h[$i] > $h[$y]) {
                $y--;
            } else {
                $i++;
            }
        }

        return $mA;
    }
}