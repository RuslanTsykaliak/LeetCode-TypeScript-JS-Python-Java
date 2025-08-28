class Solution {

    /**
     * @param Integer[][] $grid
     * @return Integer[][]
     */
    function sortMatrix($grid) {
        $len = sizeof($grid);
        for ($a = 0; $a < $len - 1; $a++) {
            $toprigh = [];
            $botleft = [];
            for ($b = 0; $b < $len - $a; $b++) {
                $botleft[$b] = $grid[$b + $a][$b];
                if ($a > 0)
                    $toprigh[$b] = $grid[$b][$b + $a];
            }
            rsort($botleft);
            sort($toprigh);
            for ($b = 0; $b < $len - $a; $b++) {
                $grid[$b + $a][$b] = $botleft[$b];
                if ($a > 0)
                    $grid[$b][$b + $a] = $toprigh[$b];
            }
        }
        return $grid;
    }
}