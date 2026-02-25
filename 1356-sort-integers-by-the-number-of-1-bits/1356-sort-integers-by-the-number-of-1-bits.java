class Solution {
    public int[] sortByBits(int[] arr) {
        int res[] = Arrays.stream(arr)
                .boxed()
                .sorted((a, b) -> Integer.bitCount(a) == Integer.bitCount(b) ? a - b
                        : Integer.bitCount(a) - Integer.bitCount(b))
                .mapToInt(Integer::intValue)
                .toArray();
        return res;
    }
}