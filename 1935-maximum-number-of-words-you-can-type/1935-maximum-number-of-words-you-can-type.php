class Solution {

    /**
     * @param String $text
     * @param String $brokenLetters
     * @return Integer
     */
    function canBeTypedWords($text, $brokenLetters) {
        $words = explode(" ", $text);
        $result = count($words);
        $letters = str_split($brokenLetters);

        foreach ($words as $word) {
            foreach ($letters as $letter) {
                if (strpos($word, $letter) !== false) {
                    $result--;
                    break;
                }
            }
        }
        return $result;
    }
}