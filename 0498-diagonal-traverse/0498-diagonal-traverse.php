class Solution {

    /**
     * @param int [][] $mat
     * @return int []
     */
    public function findDiagonalOrder(array $mat): array
    {
        $rows = count($mat);
        $column = count($mat[0]);
        $result = [];
        
        for($diagonalSum = 0; $diagonalSum < $rows + $column - 1; $diagonalSum++) {
            if ($diagonalSum % 2 !== 0) {
                $j = min($diagonalSum, $column - 1);
                $i = $diagonalSum - $j;
                while($j >= 0 && $i < $rows) {
                    $result[] = $mat[$i][$j];
                    $j--;
                    $i++;
                }
            } else {
                $i = min($diagonalSum, $rows - 1);
                $j = $diagonalSum - $i;
                   while($j < $column && $i >= 0) {
                    $result[] = $mat[$i][$j];
                    $j++;
                    $i--;
                }
            }
        }
        
        return $result;
    }
}