class Solution {

    /**
     * @param Integer[][] $points
     * @return Float
     */
    function largestTriangleArea($points) {
        $res = 0;
        for($i=0;$i<count($points)-2;$i++){
            for($j=$i+1;$j<count($points)-1;$j++){
                for($k=$j+1;$k<count($points);$k++){
                    $cur = 0.5 * abs($points[$i][0] * ($points[$j][1]-$points[$k][1]) + $points[$j][0] * ($points[$k][1]-$points[$i][1]) + $points[$k][0] * ($points[$i][1]-$points[$j][1]));
                    $res = max($res,$cur);
                }
            }   
        }
        return $res;
    }
}