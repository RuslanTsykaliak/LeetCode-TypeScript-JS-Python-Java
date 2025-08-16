class Solution {

    /**
     * @param Integer $num
     * @return Integer
     */
    function maximum69Number ($num) {
        $digits = str_split((string)$num);
        echo $digits;
        for ($i = 0; $i < count($digits); $i++) {
            if ($digits[$i] === '6') {
                $digits[$i] = '9';
                break; // Solo cambiar el primer 6
            }
        }
        $intBack = (int)implode('', $digits);
        return $intBack;
    }
}