class Solution {

    /**
     * @param String $s
     * @return Integer
     */
    function countPalindromicSubsequence($s) {
        $ans = 0;
        $n = strlen($s);

        // Array to store first and last occurrences of each character
        $positions = [];

        for ($i = 0; $i < $n; $i++) {
            if (!isset($positions[$s[$i]])) {
                $positions[$s[$i]] = [$i, $i];
            } else {
                $positions[$s[$i]][1] = $i;
            }
        }

        foreach ($positions as $ch => $range) {
            $left = $range[0];
            $right = $range[1];

            if ($right - $left <= 1) {
                continue; // No valid subsequences in this range
            }

            $uniqueChars = [];
            for ($i = $left + 1; $i < $right; $i++) {
                $uniqueChars[$s[$i]] = true; // Store unique characters
            }

            $ans += count($uniqueChars); // Count the unique characters
        }

        return $ans;
    }
}