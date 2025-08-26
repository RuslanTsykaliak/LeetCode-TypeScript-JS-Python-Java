class Solution {

    /**
     * @param Integer[][] $dimensions
     * @return Integer
     */
    function areaOfMaxDiagonal($dimensions) {
        $diag = -1;
        $area = -1;

        foreach ($dimensions as [$b, $c]) {
            $len = sqrt($b ** 2 + $c ** 2);
            if ($len > $diag) {
                $diag = $len;
                $area = $b * $c;
            } elseif ($len == $diag && ($b * $c) > $area) {
                $area = ($b * $c);
            }
        }
        return $area;
    }
}