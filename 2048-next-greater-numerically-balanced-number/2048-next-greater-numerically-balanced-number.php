class Solution {

    /**
     * @param Integer $n
     * @return Integer
     */
    function nextBeautifulNumber($n) {
        while (true) {
            $n++;
            $a = array_count_values(str_split($n));
            foreach ($a as $k => $v) {
                if ($k != $v) continue 2;
            }
            return $n;
        }
    }
}