class Solution {
    public int findTheDistanceValue(int[] arr1, int[] arr2, int d) {
        int cnt = 0;
        for (int x : arr1) { // look at each x
            boolean ok = true; // assume x is "far from everything"
            for (int y : arr2) { // compare against every y
                if (Math.abs(x - y) <= d) {
                    ok = false; // found one that's too close
                }
            }
            if (ok) cnt++; // x survived, count it
        }
        return cnt;
    }
}