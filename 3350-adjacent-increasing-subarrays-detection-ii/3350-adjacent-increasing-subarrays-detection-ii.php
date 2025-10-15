class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function maxIncreasingSubarrays($nums) {
        [$res, $precnt, $cnt] = [0,0,1];
        for ($i = 1; $i <= count($nums) - 1; $i++) {
            if ($nums[$i] > $nums[$i - 1]) {
                $cnt++;
            } else {
                $precnt = $cnt;
                $cnt = 1;
            }

            if ($precnt === $cnt) {
                $maxStep = $cnt;
            } elseif (abs($precnt - $cnt) >= min($precnt, $cnt)) {
                $maxStep = max($cnt, $precnt);
                $maxStep = floor($maxStep / 2);
            } else {
                $maxStep = min($cnt, $precnt);
            }

            $res = max($res, $maxStep);
        }

        return $res;
    }
}