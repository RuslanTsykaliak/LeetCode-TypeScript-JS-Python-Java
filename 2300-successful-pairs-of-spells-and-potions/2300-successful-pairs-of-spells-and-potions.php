class Solution {

    /**
     * @param Integer[] $spells
     * @param Integer[] $potions
     * @param Integer $success
     * @return Integer[]
     */
    function successfulPairs($spells, $potions, $success) {
        $n = count($spells);
        $m = count($potions);
        $pairs = array_fill(0, $n, 0);
        sort($potions);

        for ($i = 0; $i < $n; $i++) {
            $spell = $spells[$i];
            $left = 0;
            $right = $m - 1;

            while ($left <= $right) {
                $mid = $left + (int)floor(($right - $left) / 2);
                $product = (int)$spell * (int)$potions[$mid];
                if ($product >= $success) {
                    $right = $mid - 1;
                } else {
                    $left = $mid + 1;
                }
            }
            $pairs[$i] = $m - $left;
        }
        return $pairs;
    }
}