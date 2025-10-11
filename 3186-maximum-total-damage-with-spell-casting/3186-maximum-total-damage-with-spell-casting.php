class Solution {

    /**
     * @param Integer[] $power
     * @return Integer
     */
    function maximumTotalDamage($power) {
        sort($power);
        $dp = [];
        $preMax = 0;
        $ans = 0;
        $dpIdx = 0;

        for ($i = 0; $i < count($power);) {
            while ($dpIdx < count($dp) && $dp[$dpIdx][0] + 2 < $power[$i]) {
                $preMax = max($preMax, $dp[$dpIdx][1]);
                $dpIdx++;
            }

            $j = $i;
            $cur = 0;
            while ($j < count($power) && $power[$j] == $power[$i]) {
                $cur += $power[$j];
                $j++;
            }

            $ans = max($ans, $cur + $preMax);
            $dp[] = [$power[$i], $cur + $preMax];
            $i = $j;
        }

        return $ans;
    }
}