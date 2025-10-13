class Solution {

    /**
     * @param String[] $words
     * @return String[]
     */
    function removeAnagrams($words) {
        $left = 0;
        $right = 1;
        while(isset($words[$right]) ){
            // Check if the word is anagram
            if($this->isAnagram($words[$left], $words[$right])){
                unset($words[$right]);
            }
            else{
                $left = $right;
            }
            $right++;
        }
        return $words;


    }

    function isAnagram($word1, $word2){
        $w1 = str_split($word1); sort($w1);
        $w2 = str_split($word2); sort($w2);

        $word1 = implode('', $w1);
        $word2 = implode('', $w2);

        return $word1 === $word2;

    }
}