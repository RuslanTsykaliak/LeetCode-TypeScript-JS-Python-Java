class Solution {
    public List<List<Integer>> minimumAbsDifference(int[] arr) {
        Arrays.sort(arr);
        int n = arr.length;
        int min_diff = Integer.MAX_VALUE;
        for (int i = 0; i < n - 1; i++){
            min_diff = Math.min(min_diff, arr[i + 1] - arr[i]);
        }
        List<List<Integer>> res = new ArrayList<>();
        for (int i = 0; i < n - 1; i++){
            if (arr[i + 1] - arr[i] == min_diff){
                res.add(Arrays.asList(arr[i], arr[i + 1]));
            }
        }
        return res;
    }
}