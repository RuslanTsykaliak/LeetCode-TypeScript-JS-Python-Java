class Solution {

    /**
     * @param Integer $n
     * @return Integer
     */
    function totalMoney($n) {
        $fullWeeks = intval($n / 7);
        $daysOver = $n % 7;

        return $daysOver * ((1 + 2 * $fullWeeks + $daysOver) / 2) // sum of days of partial week
            + 28 * $fullWeeks // 7 * ((1 + 7) / 2) -- 1 + .. + 7 for each week
            + ($fullWeeks > 0 ? (7 * ($fullWeeks * ($fullWeeks - 1) / 2)) : 0) // additional 1 per every full week
            ;
    }
}