class Solution {

    /**
     * @param Integer $n
     * @return Integer[]
     */
    function sumZero($n) {
        $res=[];
        if($n % 2 != 0) $res[] = 0; 
        for($i=1; $i<=floor($n/2); $i++) {
            $res[] = $i;
            $res[] = $i*-1;
        }
        return $res;
    }
}