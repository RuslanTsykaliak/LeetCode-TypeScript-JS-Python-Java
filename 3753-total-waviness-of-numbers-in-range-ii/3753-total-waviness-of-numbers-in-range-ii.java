class Solution {

    static class State {

        int prev, curr, tight, lead;
        long cnt, sum;

        State(int prev, int curr, int tight, int lead, long cnt, long sum) {
            this.prev = prev;
            this.curr = curr;
            this.tight = tight;
            this.lead = lead;
            this.cnt = cnt;
            this.sum = sum;
        }
    }

    private long solve(long num) {
        // if the number has fewer than 3 digits, the fluctuation value is 0
        if (num < 100) {
            return 0;
        }
        String str = Long.toString(num);
        int n = str.length();

        List<State> currStates = new ArrayList<>();
        // digit 10 represents the invalid state when there is a leading zero
        currStates.add(new State(10, 10, 1, 1, 1, 0));

        for (int pos = 0; pos < n; ++pos) {
            int limit = str.charAt(pos) - '0';
            long[][][][] cnt = new long[2][2][11][11];
            long[][][][] sum = new long[2][2][11][11];

            for (State st : currStates) {
                int maxDigit = st.tight == 1 ? limit : 9;
                for (int digit = 0; digit <= maxDigit; ++digit) {
                    int newLead = (st.lead == 1 && digit == 0) ? 1 : 0;
                    int newPrev = st.curr;
                    int newCurr = newLead == 1 ? 10 : digit;
                    int newTight = (st.tight == 1 && digit == maxDigit) ? 1 : 0;

                    long add = 0;
                    // calculate fluctuation only when there are three significant digits (both prev and curr are valid and not leading zeros)
                    if (newLead == 0 && st.prev != 10 && st.curr != 10) {
                        if ((st.prev < st.curr && st.curr > digit) ||
                                (st.prev > st.curr && st.curr < digit)) {
                            add = st.cnt;
                        }
                    }

                    cnt[newTight][newLead][newPrev][newCurr] += st.cnt;
                    sum[newTight][newLead][newPrev][newCurr] += st.sum + add;
                }
            }

            // collect legal states
            List<State> nextStates = new ArrayList<>();
            for (int tight = 0; tight < 2; ++tight) {
                for (int lead = 0; lead < 2; ++lead) {
                    for (int prev = 0; prev <= 10; ++prev) {
                        for (int curr = 0; curr <= 10; ++curr) {
                            long c = cnt[tight][lead][prev][curr];
                            long s = sum[tight][lead][prev][curr];
                            // if the current state is valid, proceed to the next round of calculation
                            if (c != 0) {
                                nextStates.add(
                                        new State(prev, curr, tight, lead, c, s));
                            }
                        }
                    }
                }
            }

            currStates = nextStates;
        }

        // sum of fluctuation values of all valid states
        long ans = 0;
        for (State st : currStates) {
            ans += st.sum;
        }
        return ans;
    }

    public long totalWaviness(long num1, long num2) {
        return solve(num2) - solve(num1 - 1);
    }
}