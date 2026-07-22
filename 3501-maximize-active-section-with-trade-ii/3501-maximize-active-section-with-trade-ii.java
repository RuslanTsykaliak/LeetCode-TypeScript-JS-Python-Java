class SparseTable {

    private List<List<Integer>> st;

    public SparseTable(List<Integer> data) {
        st = new ArrayList<>();
        st.add(new ArrayList<>(data));
        int i = 1,
                N = st.get(0).size();
        while (2 * i <= N + 1) {
            List<Integer> pre = st.get(st.size() - 1);
            List<Integer> cur = new ArrayList<>();
            for (int j = 0; j < N - 2 * i + 1; j++) {
                cur.add(Math.max(pre.get(j), pre.get(j + i)));
            }
            st.add(cur);
            i <<= 1;
        }
    }

    public int query(int begin, int end) {
        if (begin > end) {
            return 0;
        }
        int len = end - begin + 1;
        int lg = 31 - Integer.numberOfLeadingZeros(len);
        return Math.max(
                st.get(lg).get(begin),
                st.get(lg).get(end - (1 << lg) + 1));
    }
}

class Solution {

    public List<Integer> maxActiveSectionsAfterTrade(
            String s,
            int[][] queries) {
        int n = s.length();
        int cnt1 = 0;
        for (char c : s.toCharArray()) {
            if (c == '1')
                cnt1++;
        }

        List<Integer> zeroBlocks = new ArrayList<>();
        List<Integer> blockLeft = new ArrayList<>();
        List<Integer> blockRight = new ArrayList<>();

        int i = 0;
        while (i < n) {
            int st = i;

            while (i < n && s.charAt(i) == s.charAt(st)) {
                i += 1;
            }

            if (s.charAt(st) == '0') {
                zeroBlocks.add(i - st);
                blockLeft.add(st);
                blockRight.add(i - 1);
            }
        }

        int m = zeroBlocks.size();
        if (m < 2) {
            // continuous 0 blocks less than 2 segments, return the answer directly
            List<Integer> result = new ArrayList<>();
            for (int q = 0; q < queries.length; q++) {
                result.add(cnt1);
            }
            return result;
        }

        List<Integer> tmpSum = new ArrayList<>();
        for (int k = 0; k < m - 1; k++) {
            tmpSum.add(zeroBlocks.get(k) + zeroBlocks.get(k + 1));
        }
        SparseTable st = new SparseTable(tmpSum);
        List<Integer> ans = new ArrayList<>();

        for (int[] q : queries) {
            int l = q[0],
                    r = q[1];
            int idx = lowerBound(blockRight, l);
            int jdx = upperBound(blockLeft, r) - 1;

            // at most 1 continuous block of 0s within the substring
            if (idx > m - 1 || jdx < 0 || idx >= jdx) {
                ans.add(cnt1);
                continue;
            }

            int firstLen = blockRight.get(idx) - Math.max(blockLeft.get(idx), l) + 1; // actual length of the first consecutive block of 0s in the substring
            int lastLen = Math.min(blockRight.get(jdx), r) - blockLeft.get(jdx) + 1; // actual length of the last consecutive block of 0s in the substring
            // exactly 2 consecutive 0 blocks within the substring
            if (idx + 1 == jdx) {
                int bestGain = firstLen + lastLen;
                ans.add(cnt1 + bestGain);
                continue;
            }

            int val1 = firstLen + zeroBlocks.get(idx + 1);
            int val2 = zeroBlocks.get(jdx - 1) + lastLen;
            int val3 = st.query(idx + 1, jdx - 2);
            int bestGain = Math.max(Math.max(val1, val2), val3);
            ans.add(cnt1 + bestGain);
        }

        return ans;
    }

    private int lowerBound(List<Integer> list, int target) {
        int left = 0,
                right = list.size();
        while (left < right) {
            int mid = left + (right - left) / 2;
            if (list.get(mid) < target) {
                left = mid + 1;
            } else {
                right = mid;
            }
        }
        return left;
    }

    private int upperBound(List<Integer> list, int target) {
        int left = 0,
                right = list.size();
        while (left < right) {
            int mid = left + (right - left) / 2;
            if (list.get(mid) <= target) {
                left = mid + 1;
            } else {
                right = mid;
            }
        }
        return left;
    }
}